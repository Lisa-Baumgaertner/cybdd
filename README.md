# cybdd



## Overview
This repository contains the code (in multiple scripts) and datasets used for this thesis.
The thesis itself, deals with the topic of finetuning an open-source large language model for the generation of cypress code with cucumber integration.
In the following the folder structure and its contents are explained.

### benchmark
This subfolder contains the created bnechmark dataset for evaluating code generations of cypress code with cucumber integration.
Also the 50-sample subset of the AdvBench-dataset by Zou et al. 2023 (https://doi.org/10.48550/arXiv.2307.15043).
The benchmark dataset file (benchmark_ds.xlsx) contains multiple Sheets:
- ``benchmark:`` Contains the actual benchmark samples with the instruction, the bdd scenario. cypress code and html context.
- ``gpt-4o:`` Contains the generations from the batch inference script for model GPT-4o. 
- ``gemini-2.5-flash:`` Contains the generations from the batch inference script for model Gemini-2.5-Flash.
- ``code-llama-base:`` Contains the generations from the batch inference script for model Code-Llama Instruct 7B.
- ``deepseek-coder-6.7:`` Contains the generations from the batch inference script for model DeepSeek Coder 6.7.
- ``r8a16:`` Contains the generations from the batch inference script for model Code-Llama Instruct 7B QLoRA adapter with rank = 8 and alpha = 16.
- ``r8a32:`` Contains the generations from the batch inference script for model Code-Llama Instruct 7B QLoRA adapter with rank = 8 and alpha = 32.
- ``r16a64:`` Contains the generations from the batch inference script for model Code-Llama Instruct 7B QLoRA adapter with rank = 16 and alpha = 64.
- ``r32a128:`` Contains the generations from the batch inference script for model Code-Llama Instruct 7B QLoRA adapter with rank = 32 and alpha = 128.
- ``qwen2.5-coder:`` Contains the generations from the batch inference script for model Qwen2.5-Coder.
- ``wavecoder-ultra:`` Contains the generations from the batch inference script for model Wavecoder-Ultra.

### evaluation
This subfolder contains the code used for evaluating the code generations.
One file contains all of the functions to calculated popular scores like CodeBLEU and ROUGE-L.
The other file contains the custom code for calculating the CYBDD-score.

### inference
This subfolder contains code to perform batch inferences for the trained adapters using the benchmark dataset, the AdvBench-dataset and the base model.

### preprocessing
This subfolder contains the code to bring the training dataset into the required format.
Also contains the preprocessed dataset.

### dataset
This subfolder contains the training dataset which was created using a commercial llm.

### training
This subfodler contains the training / finetuning code.

### ui
This subfolder contains the code for a gradio ui, which can be run with enough ressources.
It is recommended to use GPU ressources, such as RunPod, otherwise inference might not work or be very slow. 


### cypress suite
This subfolder contains all of the cypress tests that make up the benchmark dataset with their repsective bdd feature files in gherkin syntax.
