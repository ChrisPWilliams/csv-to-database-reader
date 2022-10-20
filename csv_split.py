import pandas as pd

def convert_to_ints(series):
    """
    We replace each unique value in the series with an int corresponding to order of appearance.
    Then, when we compare later, columns whose unique values appear in the same order and
    same frequencies will appear identical.
    """
    replace_dict = {val : num for num, val in enumerate(series.unique())}
    return series.replace(replace_dict)

# should get csv and headers

def split_and_insert(header_csv_path, new_headers):
    main_df = 0
    if new_headers:
        main_df = pd.read_csv(header_csv_path, names=new_headers)
    else:
        main_df = pd.read_csv(header_csv_path)
    all_tables = [main_df]
    non_uniques_df = main_df.loc[:, [col for col in main_df if not main_df[col].is_unique]].copy()
    int_compare_df = non_uniques_df.transform(convert_to_ints)





    
    