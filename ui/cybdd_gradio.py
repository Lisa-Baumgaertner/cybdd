# allows to do external processes
import subprocess
import sys

# install required packages
def pip_install(package_list):
    for package in package_list:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# list of packages to install
package_list = ['transformers', 'peft', 'bitsandbytes', 'torch', 'gradio']
pip_install(package_list)

# necessary imports, placed after install
import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
from peft import PeftModel, PeftConfig
import torch
from huggingface_hub import login

# use your huggingface access token  here
hf_token=" "
# login to hf
login(hf_token)

# set model to use
model_name = "meta-llama/CodeLlama-7b-Instruct-hf"



# loading th emodel etc. is done before calling the generate function
# this way the model does not need to be loaded each time the generate function is called

# get adapter you want to use from huggingface
adapter = "libaum/adapter-rank32-alpha128_final"

peft_configuration = PeftConfig.from_pretrained(adapter)


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

# load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

# load adapters into model
model = PeftModel.from_pretrained(model, adapter)


def generate(instruction, bdd, html_context, radio, radio_style):

    imperative = """
    Rules:
    1. Match the number and the position of {string} parameters exactly to the way and order they appear in the provided BDD scenario.
    2. Only use the selectors that appear in the provided HTML context. Do not hallucinate or generalize selectors.
    3. If an element has both an id and a data-* attribute, choose the data-* attribute (e.g. [data-codecept], [data-test], etc.).
    4. Use selectors with the correct structure (e.g., [data-codecept="selector"] instead of .selector or #selector), and do not invent or hallucinate new values.
    5. Do not merge multiple BDD steps into a single Cypress step.
    6. Preserve the logic and structure of each BDD step when naming the corresponding Cypress step.\n
    """

    declarative = """
    Rules:
    1. Only use the selectors that appear in the provided HTML context. Do not hallucinate or generalize selectors.
    2. If an element has both an id and a data-* attribute, choose the data-* attribute (e.g. [data-codecept], [data-test], etc.).
    3.Use selectors with the correct structure (e.g., [data-codecept="selector"] instead of .selector or #selector), and do not invent or hallucinate new values.
    4. Do not merge BDD steps. Keep each step isolated and clearly mapped.
    5. Preserve the logic and structure of each BDD step when naming the corresponding Cypress step.\n

    """

    # build prompt
    if radio_style == "declarative":
        if radio == "single page":
            prompt_text = "<s>[INST] " + instruction + '\n' + declarative + "#### Style" + '\n' + radio_style + '\n' + "#### HTML Context" + '\n' + html_context + '\n' + "#### BDD Scenario" + '\n' + bdd + " [/INST]"
        else:
            prompt_text = "<s>[INST] " + instruction + '\n' + declarative + "#### Style" + '\n' + radio_style + '\n' + "#### Multi-Page HTML Context" + '\n' + html_context + '\n' + "#### BDD Scenario" + '\n' + bdd + " [/INST]"
    if radio_style == "imperative":
        if radio == "single page":
            prompt_text = "<s>[INST] " + instruction + '\n' + imperative + "#### Style" + '\n' + radio_style + '\n' + "#### HTML Context" + '\n' + html_context + '\n' + "#### BDD Scenario" + '\n' + bdd + " [/INST]"
        else:
            prompt_text = "<s>[INST] " + instruction + '\n' + imperative + "#### Style" + '\n' + radio_style + '\n' + "#### Multi-Page HTML Context" + '\n' + html_context + '\n' + "#### BDD Scenario" + '\n' + bdd + " [/INST]"


    # generate
    model.eval()

    generate_cy = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=600,
        do_sample=False,
        return_full_text=False # sicherstellen, dass nur Generierung und nicht ganzer Prompt mit
    )

    # Inferenz
    output = generate_cy(prompt_text)[0]["generated_text"]

    return output




def clear_all_fields():
    """Clear all fields.
    """
    instruction = ""
    bdd_input = ""
    html_context = ""
    cypress_code = ""
    return instruction, bdd_input, html_context, cypress_code


theme = gr.themes.Ocean(
    primary_hue="green",
    secondary_hue="emerald",
)


context_value = ""
# gradio building blocks
with gr.Blocks(theme=theme) as demo:

    gr.Markdown("# <center> Generator for Cypress </center>")

    with gr.Row():
        #  create building blocks
        with gr.Column():
            instruction = gr.Textbox(label="Instruction", lines=4, html_attributes={"spellcheck": "false"})
            bdd_input = gr.Textbox(label="BDD Scenario", lines=8, html_attributes={"spellcheck": "false"})
            radio = gr.Radio(["single page", "multi page"], label="HTML Context Type", info="What kind of html context do you want to use?")
            radio_style = gr.Radio(["imperative", "declarative"], label="BDD Scenario Style", info="What kind of bdd style do you want to use?")
            html_input = gr.Textbox(label="HTML Context", lines=11, html_attributes={"spellcheck": "false"})
        with gr.Column():
            cypress_code = gr.Textbox(label="Cypress Code", lines=40)


    clear = gr.Button("Clear all fields", variant="secondary")
    clear.click(fn=clear_all_fields, inputs=[], outputs=[instruction, bdd_input, html_input, cypress_code])
    generate_bttn = gr.Button("Generate cy", variant="primary")
    # call generate function on button click
    generate_bttn.click(fn=generate, inputs=[instruction, bdd_input, html_input, radio, radio_style], outputs=cypress_code)


demo.launch(share=True)

