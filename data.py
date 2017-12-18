from datetime import datetime
import pandas as pd
from pandas.tools.plotting import table
import matplotlib.pyplot as plt
from models.reddit import RedditModel
from models.finance import FinanceModel

def get_data_frame(start_date, end_date, dataset, interval,
                 search_phrase, min_score, sample_size):
    reddit_model = RedditModel()
    finance_model = FinanceModel()
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
    df = finance_model.getData(dataset, start_date_obj, end_date_obj, interval)

    reddit_data = []
    prev_row = None
    time_delta = None
    for index, row in df.iterrows():
        if prev_row is None:
            prev_row = row
            continue
        if time_delta == None:
            time_delta = prev_row['Date'] - row['Date']
        response_data = reddit_model.getArticleData(
            row['Date'],
            prev_row['Date'],
            search_phrase,
            min_score,
            sample_size)
        reddit_data.append(response_data)
        prev_row = row

    response_data = reddit_model.getArticleData(
        prev_row['Date'] - time_delta,
        prev_row['Date'],
        search_phrase,
        min_score,
        sample_size)
    reddit_data.append(response_data)
    reddit_df_data = {}
    for k in response_data.keys():
        reddit_df_data[k] = []
        for row in reddit_data:
            reddit_df_data[k].append(row[k])
    df2 = pd.DataFrame(reddit_df_data, columns=['posts', 'mean', 'mode', 'median', 'm_high', 'm_low'])
    df3 = pd.concat([df, df2], axis=1)
    return df3

def plot_graph(dataframe, x_key, secondary_y=None, label=None, title='', top=None):
    if secondary_y is not None:
        ax = dataframe.plot(x=x_key, secondary_y=secondary_y, title=title)
    else:
        ax = dataframe.plot(x=x_key, title=title)

    lines, labels = ax.get_legend_handles_labels()

    if secondary_y is None:
        if label is not None:
            ax.legend(label)

    if top is not None:
        plt.subplots_adjust(top=top)
    plt.show()
