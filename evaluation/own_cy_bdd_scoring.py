import pandas as pd
from pandas import ExcelWriter


def calculate_score(path_benchmark, path_output, column):
    """Calculate the CYBDD score for the entered Sheet in Benchmark-Dataset.

    :param column: specifies the sheet that should be read from the benchmark dataset,
                   this parameter is  also used to build the column name for the CYBDD scores in new excel file
    """

    cy_score_list = list()

    # read in the file containing the necessary scores of ROUGUE-L, Function and CodeBLEU
    # in this case read the benchmark dataset
    file_path = path_benchmark#"C:\\Users\\Uni\\Desktop\\goldstandrad_ds.xlsx"

    # read in the column containing the metric scores for ROUGUE-L (C), Function (D) and CodeBLEU (F)
    # read as dataframe
    data_references = pd.read_excel(file_path , sheet_name=column, usecols="C, D, F")

    # convert the excel data to actual numbers, may be stored as strings which leads to issues
    data_references['ROUGUE-L'] = pd.to_numeric(data_references['ROUGUE-L'])
    data_references['Function'] = pd.to_numeric(data_references['Function'])
    data_references['CodeBLEU'] = pd.to_numeric(data_references['CodeBLEU'])

    # iterate over dataframe rows
    for i, row in data_references.iterrows():
        # calculate the cybdd score with the default weights
        calculate = (row['CodeBLEU'] * 0.5) + (row['ROUGUE-L'] * 0.2) + (row['Function']* 0.3)
        # append to list
        cy_score_list.append(calculate)


    # create dataframe for the calculated cybdd score
    # set column name to CY + column value
    cy_df = pd.DataFrame(cy_score_list, columns=['CY' + column])

    # write the calculated score into a new excel file
    with ExcelWriter(path_output) as writer:
        cy_df.to_excel(writer, sheet_name=column)



def main():
    calculate_score("C:\\Users\\Uni\\Desktop\\benchmark_ds.xlsx", "C:\\Users\\Uni\\Documents\\cy_score_TEST.xlsx", "wavecoder-ultra")

if __name__ == "__main__":
    main()
