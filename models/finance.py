import pandas as pd
import requests
from .base_model import DataModel
import datetime
from .reddit import RedditModel

class FinanceModel(DataModel):

    def __init__(self):
        DataModel.__init__(self, 'QUANDL')
        self.intervals = ('annual', 'quarterly', 'monthly')

    def getData(self, dataset, start_date, end_date, interval):
        params = {}
        params['api_key'] = self.api_key
        if interval not in self.intervals:
            raise Exception('Invalid interval! Accepted intervals are {}'.format(self.intervals))
        params['collapse'] = interval
        params['start_date'] = start_date.strftime('%Y-%m-%d')
        params['end_date'] = end_date.strftime('%Y-%m-%d')
        r = requests.get(
            self.api_url + dataset + '.json',
            params=params
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
                df[df_column] = pd.to_datetime(df[df_column], format='%Y-%m-%d', errors='coerce')
        return df
