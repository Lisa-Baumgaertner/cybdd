
import pandas as pd
from pandas import ExcelWriter
import evaluate
from codebleu import calc_codebleu


def calculate_bleu_score(path_benchmark, path_output, prediction_column):
    """Calculate the BLEU score for the entered Sheet in Benchmark-Dataset.
       Write the scores to the given output file.

    :param path_benchmark: the path where the benchmark dataset can be found.
    :param path_output: the path to the excel file to write the calculated BLEU scores to
    :param prediction_column: the sheet in benchmark dataset from which input is read in, to calculate the BLEU score, also used to name sheet for output.
    """
    # load bleu score
    bleu = evaluate.load("bleu")

    references_list = list()
    predictions_list = list()
    bleu_score_list = list()

    file_path = path_benchmark

    # read in column with cypress goldstandard code
    data_references = pd.read_excel(file_path , sheet_name='benchmark', usecols="I")

    for row in data_references["cypress_code"]:
        ref = list()
        # if non na
        if pd.notna(row):
            # strip trailing and leading whitespaces
            # and append to references list
            ref.append(str(row).strip())
            references_list.append(ref)

    # read in respective generations
    data_predictions = pd.read_excel(file_path , sheet_name=prediction_column, usecols="B")

    for row in data_predictions["Generation"]:
        pred = list()
        # if non na
        if pd.notna(row):
            # strip trailing and leading whitespaces
            # and append to predictions list
            pred.append(str(row).strip())
            predictions_list.append(pred)

    # iterate over both lists simultaneously
    for reference, prediction in zip(references_list, predictions_list):
        # compute bleu score
        bleu_score = bleu.compute(predictions=prediction, references=reference)
        bleu_score_list.append(bleu_score.get("bleu"))

    # create new column name
    column_name = 'BLEU' + prediction_column
    # create new dataframe with bleu scores
    bleu_df = pd.DataFrame(bleu_score_list, columns=['BLEU'])


    # write to excel file
    with ExcelWriter(path_output) as writer:
        bleu_df.to_excel(writer, sheet_name=column_name, index=False,  startcol=0)



def calculate_rougel_score(path_benchmark, path_output, prediction_column):
    """Calculate the ROUGUE-L score for the entered Sheet in Benchmark-Dataset.
       Write the scores to the given output file.

    :param path_benchmark: the path where the benchmark dataset can be found.
    :param path_output: the path to the excel file to write the calculated ROUGUE-L scores to
    :param prediction_column: the sheet in benchmark dataset from which input is read in, to calculate the ROUGUE-L score, also used to name sheet for output.
    """

    # load rouge score
    rouge = evaluate.load("rouge")

    references_list = list()
    predictions_list = list()
    rouge_score_list = list()

    file_path = path_benchmark

    # read in column with cypress goldstandard code from benchmark dataset
    data_references = pd.read_excel(file_path , sheet_name='benchmark', usecols="I")

    for row in data_references["cypress_code"]:
        ref = list()
        # if non na
        if pd.notna(row):
            # strip trailing and leading whitespaces
            # and append to references list
            ref.append(str(row).strip())
            references_list.append(ref)

    # read in respective generations
    data_predictions = pd.read_excel(file_path , sheet_name=prediction_column, usecols="B")

    for row in data_predictions["Generation"]:
        pred = list()
        # if non na
        if pd.notna(row):
            # strip trailing and leading whitespaces
            # and append to predictions list
            pred.append(str(row).strip())
            predictions_list.append(pred)

    # iterate over both lists simultaneously
    for reference, prediction in zip(references_list, predictions_list):
        # compute rouge score
        rouge_score = rouge.compute(predictions=prediction, references=reference)
        # get rougue-l
        rouge_score_list.append(rouge_score.get("rougeL"))

    # create new column name
    column_name = 'ROUGUE-L' + prediction_column
    # create new dataframe with rougue-l scores
    rougue_df = pd.DataFrame(rouge_score_list, columns=['ROUGE-L'])


    # write to excel file
    with ExcelWriter(path_output) as writer:
        rougue_df.to_excel(writer, sheet_name=column_name, index=False,  startcol=1)




def calculate_codebleu_score(path_benchmark, path_output, prediction_column):
    """Calculate the CodeBLEU score for the entered Sheet in Benchmark-Dataset.
       Write the scores to the given output file.

    :param path_benchmark: the path where the benchmark dataset can be found.
    :param path_output: the path to the excel file to write the calculated CodeBLEU scores to
    :param prediction_column: the sheet in benchmark dataset from which input is read in, to calculate the CodeBLEU score, also used to name sheet for output.
    """

    references_list = list()
    predictions_list = list()
    codebleu_score_list = list()

    file_path = path_benchmark

    # read in column with cypress goldstandard code from benchmark dataset
    data_references = pd.read_excel(file_path , sheet_name='benchmark', usecols="I")

    for row in data_references["cypress_code"]:
        ref = list()
        # if non na
        if pd.notna(row):
            # strip trailing and leading whitespaces
            # and append to references list
            ref.append(str(row).strip())
            references_list.append(ref)

    # read in respective code generations from the column
    data_predictions = pd.read_excel(file_path , sheet_name=prediction_column, usecols="B")

    for row in data_predictions["Generation"]:
        pred = list()
        # if non na
        if pd.notna(row):
            # strip trailing and leading whitespaces
            # and append to predictions list
            pred.append(str(row).strip())
            predictions_list.append(pred)

    # set language as javascript, because cypress is javasript based
    language = "javascript"


    # iterate over both lists simultaneously
    for reference, prediction in zip(references_list, predictions_list):
        # Compute CodeBLEU
        scores = calc_codebleu(prediction, reference, lang=language)
        codebleu_score_list.append(scores.get("codebleu"))

    # create new column name
    column_name = 'CodeBLEU' + prediction_column
    # create new dataframe with codebleu scores
    codebleu_df = pd.DataFrame(codebleu_score_list, columns=['CodeBLEU'])

    # write to excel file
    with ExcelWriter(path_output) as writer:
        codebleu_df.to_excel(writer, sheet_name=column_name, index=False,  startcol=2)




def main():


    #calculate_bleu_score("benchmark/benchmark_ds.xlsx", "TEST_bleu.xlsx", "qwen2.5-coder")
    #calculate_rougel_score("benchmark/benchmark_ds.xlsx", "TEST_rougel.xlsx", "wavecoder-ultra")
    calculate_codebleu_score("benchmark/benchmark_ds.xlsx", "TEST_code_bleu.xlsx", "wavecoder-ultra")



if __name__ == "__main__":
    main()
