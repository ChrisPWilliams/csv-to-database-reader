import csv_split as c_splt

my_df = c_splt.second_csv_read("C:/Users/ChrisWilliams/Documents/reader_test_csv.csv", [])
df_list, foreign_dict = c_splt.split_dataframe(my_df)