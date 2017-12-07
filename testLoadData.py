import pandas as pd

class Test():
    def getData(self, filename):
        df = pd.read_csv(filename)
        return df

filename = '~/DataScience/github_projects/Data_Science_Projects/mtg_app_original/MagicDatasets/MagicCards_7_25.csv'
test = Test()
test.getData(filename)