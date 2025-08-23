# include pip installs 
#from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
#from peft import PeftModel, PeftConfig
from huggingface_hub import login
import subprocess
import sys
import pandas as pd
#mport numpy as np
import json

def pip_install(package_list):
    for package in package_list:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


#package_list = ['transformers', 'peft', 'bitsandbytes']
#pip_install(package_list)


def hf_log_in():
    hf_token="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"
    login(hf_token)


def batch_inference(model_name):

    model_name = "meta-llama/CodeLlama-7b-Instruct-hf"
    #model_name = "meta-llama/CodeLlama-7b-hf"
    #
    # # load qlora adapters
    # adapter = "/workspace/orkspace/output"
    #
    #
    #
    # # load benchmark dataset to build the prompts
    #
    #
    # prompt_text = """<s>[INST] Produce an automated Cypress test using Cucumber from the given content and steps.
    # Make sure the user navigates to https://www.bergfreunde.de before starting. Where present, use the selector "data-codecept".
    #
    # #### HTML Context
    # <button class="flex items-center justify-center min-w-11 relative !text-black lg:!text-gray-200 cursor-pointer group" title="Gehe hier zum Kundenkonto" data-js-user-flyout-toggle="" data-mapp-click="header.login" data-codecept="userElementHeader"> </button>
    #
    # <input class="!mb-2.5" id="lgn_usr" data-codecept="username" type="email" autocomplete="email" name="lgn_usr" value="" maxlength="60" size="60" required="">
    #
    # <input id="lgn_pwd" class="password-input !mb-2.5" data-codecept="password" type="password" name="lgn_pwd" value="" required="">
    #
    # <button class="disabled:!bg-gray-700 disabled:cursor-not-allowed leading-4.5 py-3px relative inline-flex flex-auto items-center justify-center border border-solid rounded align-middle text-center transition-colors duration-100 no-underline whitespace-nowrap cursor-pointer before:content-['_'] before:absolute before:-inset-5px bg-primary uppercase hover:text-white hover:no-underline hover:bg-gray-800 focus:bg-gray-800 active:bg-gray-700 focus:text-white active:text-white text-white border-transparent h-10 text-lg font-sans w-full lg:max-w-[13.75rem] lg:mt-3.5 px-5" name="lgn_submit" data-variant="primary" data-mapp-click="account.navi.login" type="submit" data-codecept="loginButton"></button>
    #
    # #### BDD Scenario
    # Feature: Login on Bergfreunde
    #
    #   Scenario: User logs in with valid credentials
    #     Given the user opens the login flyout
    #     When the user enters their email and password
    #     When the user clicks the login button
    #     Then the user should be logged in and see their account page [/INST]"""
    #
    #
    # peft_configuration = PeftConfig.from_pretrained(adapter)
    # #base_model = peft_configuration.model_name
    #
    # bnb_config = BitsAndBytesConfig(
    #     load_in_4bit=True,
    #     bnb_4bit_use_double_quant=True,
    #     bnb_4bit_quant_type="nf4",
    #     bnb_4bit_compute_dtype="float16"
    # )
    #
    # model = AutoModelForCausalLM.from_pretrained(
    #     model_name,
    #     quantization_config=bnb_config,
    #     device_map="auto",
    #     trust_remote_code=True
    # )
    #
    #
    #
    #
    # tokenizer = AutoTokenizer.from_pretrained(model_name)
    # tokenizer.pad_token = tokenizer.eos_token
    #
    #
    # # Addapter laden
    # model = PeftModel.from_pretrained(model, adapter)
    # model.eval()


    # in loop generieren und jede Generierung in js file speichern, identifiziert via ids, die zu
    # .feature files alignen


    # 
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
        max_new_tokens=2000,
        do_sample=False,
        return_full_text=False # sicherstellen, dass nur Generierung und nicht ganzer Prompt mit
    )

    # Inferenz
    # output = generate_cy(prompt_text)[0]["generated_text"]
    # 
    # # Output
    # print("=== Generated Output ===\n")
    # print(output)


    #
    # save this into js file for each generation
    #file_path = "C:\\Users\\Uni\\Desktop\\goldstandrad_ds.xlsx"
    file_path = "workspace\\benchmark_ds.xlsx"

    # get specific columns
    # E = instruction
    # F = html_context
    # H = bdd_scenario
    data = pd.read_excel(file_path ,sheet_name='benchmark', usecols="E, F, G, H")
    #print(data.head(5))
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
                    elements = page.get("elements")#
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
                if model_name != "deepseek":
                    prompt = "<s>[INST] " + row['instruction'] + '\n' + "#### HTML Multi-Page Context" + '\n' + html_context_str + '\n' + "#### BDD Scenario" + '\n' + row['bdd_scenario'] + " [/INST]"
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

        if row['multi_page'] == 'no':
            try:
                if model_name != "deepseek":
                    prompt = "<s>[INST] " + row['instruction'] + '\n' + "#### HTML Context" + '\n' + row['html_context'] + '\n' + "#### BDD Scenario" + '\n' + row['bdd_scenario'] + " [/INST]"
                    #print(prompt)
                    prompt_list.append(prompt)
                else:
                    prompt = "### Instruction: " + row['instruction'] + '\n' + "HTML Context" + '\n' + row['html_context'] + '\n' + "BDD Scenario" + '\n' + row['bdd_scenario'] + '\n' + "### Response:"
                    #print(prompt)
                    prompt_list.append(prompt)

                #output = generate_cy(prompt)[0]["generated_text"]
            except Exception as e:
                print(f"[!] Error at row {index}:", e)






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
    package_list = ['transformers', 'peft', 'bitsandbytes']
    pip_install(package_list)
    # hugging face login
    hf_log_in()
    # inference function
    batch_inference('llama')

if __name__ == '__main__':
    sys.exit(main())  







