import subprocess
import sys

# install all necessary items from list below
def pip_install(package_list):
    for package in package_list:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# list of necessary installations
package_list = ['transformers', 'datasets', 'peft', 'bitsandbytes', 'accelerate',  'trl']
pip_install(package_list)




# actual imports after install
from datasets import load_dataset
import torch
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training, PeftModel
from transformers import AutoTokenizer, Trainer, TrainingArguments, AutoModelForCausalLM, EarlyStoppingCallback, BitsAndBytesConfig 
from trl import SFTConfig, SFTTrainer
from huggingface_hub import login



# use your own huggingface access token here
hf_token="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"
# perform login on huggingface
# required to load model, push adapters etc.
login(hf_token)


# load the training dataset
dataset = load_dataset("json", data_files="/workspace/dataset_preprocessed.jsonl")["train"] 
# split dataset into training and evaluation set
dataset = dataset.train_test_split(test_size=0.1, seed=42)
# make sure to shuffle the dataset incase there are similarities etc. due to generation with commercial llm
dataset = dataset.shuffle(seed=42)

# sort the split dataset into two datasets
training_dataset = dataset["train"]
evaluation_dataset  = dataset["test"]

# load the model from huggingface 
model_p = "meta-llama/CodeLlama-7b-Instruct-hf"

# load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_p)
tokenizer.pad_token = tokenizer.eos_token  



# Quantization configuration to use for loading the model
# 4-bit quantization
# this is part of QLoRA
# use Dettmers et al. 2023 data type nf4 (NormalFloat4)
# for computation use bfloat 16
# set as described in paper 
# uses bitsandbytes library which is quantization library with transformers integration
dquant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)


# CausalLM, because it is a decoder-only model
# this loads the model ready for usage, including weights from huggingface because from_pretrained is used
# use the quantization configuration set up in step before to load the model as quantized model
model = AutoModelForCausalLM.from_pretrained(model_p, quantization_config=dquant_config, device_map="auto")

# preprocess the quantized model for training
model = prepare_model_for_kbit_training(model)


# set up the lora configuration
# peft method that decomposes large matrix into 2 smaller ones in attention layers
# reduces the number of parameters that need to be finetuned drastically
# as specified in dettmers et al. 2023, lora is applied to all linear transformer block layers 
my_lora_config = LoraConfig(
    r=32,
    lora_alpha=128,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_dropout=0.05, # regularize overfitting
    bias="none",
    task_type="CAUSAL_LM"
)

#model = get_peft_model(model, lora_config)
#model.print_trainable_parameters()


# set configurations for the finetuning process
# / set hyperparameters
training_arguments = SFTConfig(
    output_dir="/workspace/output",
    per_device_train_batch_size=1,
    gradient_accumulation_steps=16,
    optim="paged_adamw_32bit",
    num_train_epochs=2,
    eval_strategy="steps",
    eval_steps=125,
    save_strategy="steps",
    save_steps=125, # save best checkpoint based on evaluation metric
    logging_steps=25,
    logging_strategy="steps",
    max_length=2048,
    group_by_length=True,
    save_total_limit=3,
    weight_decay=0.01,
    learning_rate=2e-4,
    fp16=True,
    metric_for_best_model="eval_loss",  # get checkpoint with best evaluation loss
    greater_is_better=False, # lower evaluation metric better
    load_best_model_at_end=True # restore best
)



# set up the SFTTrainer
# use the tokenizer, parameters and lora config
# uses completion_loss by default 
# use the previously split datasets
# 
trainer = SFTTrainer(
    model=model,
    processing_class=tokenizer,
    args=training_arguments,
    #max_seq_length=2048,
    peft_config=my_lora_config,
    #train_on_completion_only=True,
    #response_template="[/INST] ",
    #formatting_func=format_the_data,
    train_dataset=training_dataset, # data used for finetuning/training
    eval_dataset=evaluation_dataset, # data used for evaluation
    # stops the finetuning early if validation metric doesnt improve for 2 checks after another
    callbacks=[EarlyStoppingCallback(early_stopping_patience=2)],
)



# Finetuning
trainer.train()


# Speichern
model.save_pretrained("/workspace/output/rank32-alpha128") # saves configuration and weights of adapters to specified path 
tokenizer.save_pretrained("/workspace/output")


