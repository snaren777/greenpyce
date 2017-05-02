import pandas as pd
import numpy as np

class TargetEncoder(object):

    def __init__(self, columns, target, inplace=None):
        self.means_dict = {}
        self.columns = columns
        self.target = target
        self.inplace = inplace

    def fit(self, df):
        for column in self.columns:
            group = pd.groupby(df[[column, self.target]], column).mean()
            self.means_dict[column] = group.to_dict()

    def transform(self, df):
        for column in self.columns:

            if self.inplace:
                new_col_name = column
            else:
                new_col_name = column + '_target_encoding'

            missing = np.mean(np.array(list(self.means_dict[column][self.target].values())))
            df[new_col_name] = df[column].apply(lambda x : self.means_dict[column][self.target].get(x, missing))

