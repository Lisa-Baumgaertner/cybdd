import subprocess
import sys

def pip_install(package_list):
    for package in package_list:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def hf_log_in():
    from huggingface_hub import login
    # use your own token here
    hf_token=" "
    login(hf_token)


def batch_inference(modelnaming):
    from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
    import torch
    import pandas as pd
    import json


    model_name = "meta-llama/CodeLlama-7b-Instruct-hf"


    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16,
        trust_remote_code=True
    )


    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token


    model.eval()

    generate_cy = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=600,
        do_sample=False,
        return_full_text=False # sicherstellen, dass nur Generierung und nicht ganzer Prompt mit
    )


    file_path = "benchmark\\benchmark_ds.xlsx"

    # get specific columns
    # E = instruction
    # F = html_context
    # H = bdd_scenario
    data = pd.read_excel(file_path ,sheet_name='benchmark', usecols="E, F, G, H")
    # for each set of extracted columns, build one prompt from all three columns
    prompt = """"""
    prompt_list = list()
    output = []
    for index, row in data.iterrows():
        output = []
        if row['multi_page'] == 'yes':
            try:
                pages = json.loads(row['html_context'])  # List of page dicts
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
                if modelnaming != "deepseek":
                    prompt = "<s>[INST] " + row['instruction'] + '\n' + "#### HTML Multi-Page Context" + '\n' + html_context_str + '\n' + "#### BDD Scenario" + '\n' + row['bdd_scenario'] + " [/INST]"
                    prompt_list.append(prompt)
                else:
                    prompt = "### Instruction: " + row['instruction'] + '\n' + "HTML Multi-Page Context" + '\n' + html_context_str + '\n' + "BDD Scenario" + '\n' + row['bdd_scenario'] + '\n' + "### Response:"
                    prompt_list.append(prompt)

            except Exception as e:
                print("Error", e)

        if row['multi_page'] == 'no':
            try:
                if modelnaming != "deepseek":
                    prompt = "<s>[INST] " + row['instruction'] + '\n' + "#### HTML Context" + '\n' + row['html_context'] + '\n' + "#### BDD Scenario" + '\n' + row['bdd_scenario'] + " [/INST]"
                    prompt_list.append(prompt)
                else:
                    prompt = "### Instruction: " + row['instruction'] + '\n' + "HTML Context" + '\n' + row['html_context'] + '\n' + "BDD Scenario" + '\n' + row['bdd_scenario'] + '\n' + "### Response:"
                    prompt_list.append(prompt)

            except Exception as e:
                print("Error", e)


    # do generation and save the generation to a ".js" file 
    file_id = 1
    for prompt in prompt_list:
        output = generate_cy(prompt)[0]["generated_text"]
        filename = "sample_" + str(file_id) + ".js"
        with open("workspace\\baseline_code_llama\\" + filename, "x", encoding="utf-8") as f:
            f.write(output)
            print(output)
            file_id += 1


# main methode
def main():
    # install necessary dependencies
    package_list = ['transformers', 'bitsandbytes', 'torch', 'huggingface_hub', 'pandas', 'openpyxl']
    pip_install(package_list)
    # hugging face login
    hf_log_in()
    # inference function
    batch_inference('llama')

if __name__ == '__main__':
    sys.exit(main())  







