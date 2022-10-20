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

def split_to_dataframes(header_csv_path, new_headers):
    """
    Arguments:
        header_csv_path : String containing path to csv file
        new_headers : list containing user-defined column headings (empty list if headers already present)
    Returns:
        df_list : list of dataframes ready for insertion to sql
        foreign_keys : dict containing mappings of foreign keys between tables
    """
    main_df = 0
    if new_headers:
        main_df = pd.read_csv(header_csv_path, names=new_headers)
    else:
        main_df = pd.read_csv(header_csv_path)
    non_uniques_df = main_df.loc[:, [col for col in main_df if not main_df[col].is_unique]].copy()
    int_compare_df = non_uniques_df.transform(convert_to_ints)
    new_col_list = list(non_uniques_df.columns)
    tables = [main_df]
    already_checked_cols = [] 
    for col in new_col_list:
        new_table_cols = [col]
        already_checked_cols.append(col)
        for new_col in new_col_list:
            if new_col not in already_checked_cols:
                if int_compare_df[new_col].compare(int_compare_df[col], keep_shape=True)["self"].all():
                    new_table_cols.append(new_col)
        if new_table_cols == [col]:
            print("escape!")
            continue
        new_table = main_df.loc[:, new_table_cols].drop_duplicates()
        tables.append(new_table)
        print(new_col_list)
    for table in tables:
        print(table)
        print("\n\n")



        
        





    
    