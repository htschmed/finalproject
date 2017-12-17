import pandas as pd
import requests
import matplotlib.pyplot as plt
from data import DataModel

class FinanceModel(DataModel):

    def __init__(self):
        DataModel.__init__(self, 'QUANDL')

    def show_graph(self, dataset, params={}, label=None, title=''):
        params['api_key'] = self.api_key
        r = requests.get(
            self.api_url + dataset + '.json',
            params = params
        )
        response = r.json()
        column_index = 0
        columns_list = response['dataset']['column_names']
        dataset = response['dataset']
        data = {}
        for column in columns_list:
            data[column] = [item[column_index] for item in dataset['data']]
            column_index = column_index + 1
        df = pd.DataFrame(data, columns=columns_list)
        for df_column in df.keys():
            if df_column.lower() == 'date':
                df[df_column] = pd.to_datetime(df[df_column])
        ax = df.plot(x='Date', y='Value', title=title)
        if label is not None:
            ax.legend([label])
        plt.show()