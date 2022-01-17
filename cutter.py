import pandas as pd


class Parser:
    """gets a data set (dict) and returns only a columns that specified, if none set returns all data"""
    def __init__(self, data):
        self.df = pd.DataFrame.from_dict(data)

    def return_columns(self, *args):
        columns_for_return = list(args)
        df = self.df[columns_for_return]
        return df
