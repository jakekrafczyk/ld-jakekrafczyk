import pandas as pd

def set_display(columns, rows):
    pd.set_option('display.max_columns',columns)
    pd.set_option('display.max_rows',rows)


def list_to_column(df,new_list,column_name):
    df[column_name] = new_list
    return df