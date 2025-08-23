
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

# load tokenizer of pretrained model
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

# load adapters into model
model = PeftModel.from_pretrained(model, adapter)




# signals generate and not train
model.eval()

# generation pipeline
generate_cy = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=300,
    do_sample=False,
    return_full_text=False # sicherstellen, dass nur Generierung und nicht ganzer Prompt mit
)

# Inferenz
#output = generate_cy(prompt_text)[0]["generated_text"]
# decode

# path o benchmark dataset
file_path = "workspace\\benchmark_ds.xlsx"

# get specific columns
# E = instruction
# F = html_context
# H = bdd_scenario
data = pd.read_excel(file_path ,sheet_name='benchmark', usecols="C, E, F, G, H")
#print(data.head(5))
# for each set of extracted columns, build one prompt from all three columns
prompt = """"""
prompt_list = list()
output = []
for index, row in data.iterrows():
    output = []
    # build the prompts from benchmark dataset columns

    # if it is a multipage samples
    if row['multi_page'] == 'yes':
        try:
            # load as json to access elements later
            pages = json.loads(row['html_context'])  # List of page dicts
            # fore multipage context build the shortened version like in preprocessing
            for page in pages:
                name = page.get("name")
                elements = page.get("elements")
                output.append("Page title: " + name)
                for el in elements:
                    element_type = el.get("type")
                    sel_type = el.get("selector_type")
                    sel = el.get("selector")
                    text = el.get("text")

                    non_child = element_type + "[" + sel_type + "=" + '"' + sel + '"' + "] "

                    if text:
                        non_child += "with text " + '"' + text + '"'

                    output.append(non_child)
                    # if there are child elements, include them
                    if "children" in el:
                        for child_element in el["children"]:
                            ch_type = child_element.get("type", "")
                            ch_sel_type = child_element.get("selector_type", "")
                            ch_sel = child_element.get("selector", "")
                            ch_text = child_element.get("text")

                            child = "\t child element: " + ch_type + "[" + ch_sel_type + "=" + '"' + ch_sel + '"' + "] "

                            if text:
                                child += "with text " + '"' + ch_text + '"'

                            output.append(child)

            html_context_str = "\n".join(output)
            if model_name != "deepseek":
                prompt = "<s>[INST] " + row['instruction'] + '\n' + "#### Style" + '\n' + row['type'] + '\n' + "#### HTML Multi-Page Context" + '\n' + html_context_str + '\n' + "#### BDD Scenario" + '\n' + row['bdd_scenario'] + " [/INST]"
                prompt_list.append(prompt)
            else:
                prompt = "### Instruction: " + row['instruction'] + '\n' + "HTML Multi-Page Context" + '\n' + html_context_str + '\n' + "BDD Scenario" + '\n' + row['bdd_scenario'] + '\n' + "### Response:"
                prompt_list.append(prompt)
            #output = generate_cy(prompt)[0]["generated_text"]
            #print(prompt)

        # except Exception as e:
        #     print(f"[!] Error at row {index}:", e)
        except json.JSONDecodeError as e:
            print(f"[!] Error at row {index}: {e}")
            print("Raw content:")
            print(repr(row['html_context']))


    # if it is not a multipage sample
    if row['multi_page'] == 'no':
        try:
            if model_name != "deepseek":
                prompt = "<s>[INST] " + row['instruction'] + '\n' + "#### Style" + '\n' + row['type'] + '\n' + "#### HTML Context" + '\n' + row['html_context'] + '\n' + "#### BDD Scenario" + '\n' + row['bdd_scenario'] + " [/INST]"
                #print(prompt)
                prompt_list.append(prompt)
            else:
                prompt = "### Instruction: " + row['instruction'] + '\n' + "HTML Context" + '\n' + row['html_context'] + '\n' + "BDD Scenario" + '\n' + row['bdd_scenario'] + '\n' + "### Response:"
                #print(prompt)
                prompt_list.append(prompt)

            #output = generate_cy(prompt)[0]["generated_text"]
        except Exception as e:
            print(f"[!] Error at row {index}:", e)





file_id = 1
# set return_full_text = False to just get the generation, not the prompt
for prompt in prompt_list:
    output = generate_cy(prompt)[0]["generated_text"]
    filename = "sample_" + str(file_id) + ".js"

    with open("workspace\\r8a16_multi_dec\\" + filename, "x", encoding="utf-8") as f:
        f.write(output)
        print(output)
        file_id += 1




  





