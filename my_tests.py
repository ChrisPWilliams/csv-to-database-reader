import csv_split as c_splt

path = "C:/Users/ChrisWilliams/Documents/training_sessions_data/pp-monthly-update-new-version.csv"
headers = ["AAAAA", "BBBBB", "CCCCC", "DDDDD", "EEEEE", "FFFFF", "GGGGG", "HHHHH", "IIIII", "JJJJJ",
 "KKKKK", "LLLLL", "MMMMM", "NNNNN", "OOOOO", "PPPPP"]

my_df = c_splt.second_csv_read(path, headers)
df_dict, foreign_dict = c_splt.split_dataframe(my_df)

for df_name, df in df_dict.items():
    print(f"Table {df_name}:")
    print(df)
    print("\n\n")