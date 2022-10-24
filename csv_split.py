import pandas as pd

def convert_to_ints(series):
    """
    Arguments:
    series : pandas Series containing data
    -----
    Returns:
    new_series : pandas Series containing integers corresponding to order of appearance of each different element
    -----
    We replace each unique value in the series with an int corresponding to order of appearance.
    Then, when we compare later, columns whose unique values appear in the same order and
    same frequencies will appear identical.
    """
    print(f"preparing replace dict for {series}:")
    replace_dict = {val : num for num, val in enumerate(series.unique())}
    print("successfully generated replace dict")
    new_series = series.map(replace_dict.get)
    print("successful replace")
    return new_series

def second_csv_read(header_csv_path, new_headers):
    """
    Arguments:
        header_csv_path : String containing path to csv file
        new_headers : list containing user-defined column headings (empty list if headers already present)
    Returns:
        main_df : dataframe
    """
    main_df = 0
    if new_headers:
        main_df = pd.read_csv(header_csv_path, names=new_headers)
    else:
        main_df = pd.read_csv(header_csv_path)
    return main_df

def split_dataframe(main_df):
    """
    Arguments:
        main_df : Pandas dataframe
    Returns:
        df_dict : dict containing names and dataframes ready for insertion by sql
    """
    print("beginning split")
    non_uniques_df = main_df.loc[:, [col for col in main_df if not main_df[col].is_unique]].copy()
    print("identified non-unique columns")
    int_compare_df = non_uniques_df.transform(convert_to_ints)
    new_col_list = list(non_uniques_df.columns)
    df_dict = {}
    already_checked_cols = []
    print("beginning comparison loop sequence") 
    for col in new_col_list:
        print(f"comparing for {col}")
        new_table_cols = [col]
        already_checked_cols.append(col)
        for new_col in new_col_list:
            print(f"nested loop checking {col} against {new_col}")
            if new_col not in already_checked_cols:
                if int_compare_df[new_col].compare(int_compare_df[col], keep_shape=True)["self"].all():
                    new_table_cols.append(new_col)
        if new_table_cols == [col]:
            continue
        new_table = main_df.loc[:, new_table_cols].drop_duplicates()
        new_table_name = str(new_table.columns[0][:4])
        df_dict[new_table_name] = new_table             # pretty sure new_table_name is guaranteed to be unique but there is no check
    # for table in df_dict.values():
        # print(table)
        # print("\n\n")
    print("subtable extraction complete!")

    # should probably throw out subtables where the length of the subtable is more than half the length of the main table

    # foreign_dict looks like {foreign_key : primary_key}
    # for table insertion: primary keys shall be named <table_name>_id

    main_copy = main_df.copy()
    foreign_dict = {}
    for df_name, df in df_dict.items():
        main_copy.insert(len(main_copy.columns), f"{df_name}_foreign_key", int_compare_df[df.columns[0]])
        main_copy.drop(columns=df.columns)
        foreign_dict[f"{df_name}_foreign_key"] = f"{df_name}_id"
    df_dict["main_table"] = main_copy
    return df_dict, foreign_dict
    



        
        





    
    