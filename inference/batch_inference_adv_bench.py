
import subprocess
import sys


def pip_install(package_list):
    for package in package_list:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


package_list = ['transformers', 'peft', 'bitsandbytes', 'torch', 'pandas', 'openpyxl']
pip_install(package_list)

#import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
from peft import PeftModel, PeftConfig
import torch
from huggingface_hub import login
import pandas as pd
import json

hf_token="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"

login(hf_token)

# set model
model_name = "meta-llama/CodeLlama-7b-Instruct-hf"

# set adapter
adapter = "libaum/adapter-rank8-alpha16-final"


# get configuration from adapter
peft_configuration = PeftConfig.from_pretrained(adapter)

# build qlora configuration for loading the pretrained model quantized
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype="float16"
)

# load model quantized
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True
)

# load tokenizer for the pretrained model
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

# load adapters into model
model = PeftModel.from_pretrained(model, adapter)




# signals generate and not train

model.eval()


# generation pipeline 
# set return_full_text = False to just get the generation, not the prompt
generate_cy = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=600, # number of new tokens generated, set this to 600, because with 300 code may be cut off
    do_sample=False,
    return_full_text=False # sicherstellen, dass nur Generierung und nicht ganzer Prompt mit
)

# Inferenz
#output = generate_cy(prompt_text)[0]["generated_text"]
# decode


# file path of the adv benchmark dataset to load
file_path = "workspace\\"

# get specific column containing the prompts in the adv bench dataset
# A: prompt
prompt_list = list()
data = pd.read_excel(file_path ,sheet_name='advbench_samples', usecols="A")

# itereate over the prompts and bring them into the format
for index, row in data.iterrows():
    ds_prompt = row['prompt']
    final_prompt = "<s>[INST] " + ds_prompt +  " [/INST]"
    prompt_list.append(final_prompt)



file_id = 1
# for each built prompt get generation and write to a ".txt" file
for prompt in prompt_list:
    output = generate_cy(prompt)[0]["generated_text"]
    filename = "sample_" + str(file_id) + ".txt"
    with open("workspace\\r8a16_adv\\" + filename, "x", encoding="utf-8") as f:
        f.write(output)
        print(output)
        file_id += 1




  





