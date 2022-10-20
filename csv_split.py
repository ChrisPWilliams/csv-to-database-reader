import pandas as pd

def convert_to_ints(series):
    replace_dict = {val : num for num, val in enumerate(series.unique())}
    series.replace()




# should get csv and headers

def split_and_insert(header_csv_path, new_headers):
    main_df = 0
    if new_headers:
        main_df = pd.load_csv(header_csv_path, names=new_headers)
    else:
        main_df = pd.load_csv(header_csv_path)
    all_tables = [main_df]
    non_uniques_df = main_df.loc[:, [col for col in main_df if not col.is_unique]].copy()





    
    