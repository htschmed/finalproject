# Installation
Requires Python 3.5 or greater. Install packages using the following command after cloning the repo:

`pip install -r requirements.txt`

A configuration file called *config.ini* is also required to be placed in the root directory.  See the example ini file for settings

Once setup you may run the sample main program by entering the following command:

`python main.py`

Demo at https://youtu.be/XiP74QLCn2Q

# Function Definitions
## data.get_data_frame(start_date, end_date, dataset, interval,search_phrase, min_score, sample_size)
**Arguments**

*start_date:* start date of time perid to analyze, this is a string in the format of %Y-%m-%d 

*end_date:* end date of of time perid to analyze, this is a string in the format of %Y-%m-%d

*dataset:* dataset code found at https://www.quandl.com/search

*interval:* string that specifies the data point intervals.  Acceptable values are "annual", "quarterly", "monthly"

*search_phrase:* string that specifies the reddit search phrase to find in post titles for statistical analysis

*min_score:* minimum score of reddit posts to include in search query

*sample_size:* maximum number of reddit posts to pull for score analysis. Sample will always start with highest scores first

**Return Value**

Function returns a pandas dataframe with the following columns:

*Date:* date of quandl dataset series
*Value:* value of quandl dataset series

These columns are an aggregation of reddit data from previous row date to current row date 

*posts:* total number or reddit posts

*mean:* mean score of sampled posts

*mode:* mode score of sampled posts

*median:* median score of sampled posts

*m_high:* high median score of sampled posts

*m_low:* low median score of sampled posts

## data.plot_graph(dataframe, x_key, secondary_y=None, label=None, title='', top=None)

**Arguments**

*dataframe:* dataframe source from quandl time series dataset to plot a line graph

*x_key:* column that should be mapped to the x-axis

*secondary_y:* list of columns that can be added as a scaled secondary axis to y

*label:* label the line data in the legend

*title:* give a title to the graph

*top:* adjust top of plot offset (useful for fitting long titles)

# Sample Usage

<pre>
>>> from data import get_data_frame, plot_graph
from data import get_data_frame, plot_graph
>>> df = get_data_frame('2009-1-1', '2017-12-1', 'BCHAIN/MKPRU', 'annual', 'bitcoin', 100, 100)
df = get_data_frame('2009-1-1', '2017-12-1', 'BCHAIN/MKPRU', 'annual', 'bitcoin', 100, 100)
>>> print(df)
print(df)
        Date         Value  total   mean  mode  median  m_high  m_low
0 2017-12-31  10147.370000   6666  101.5   101   101.5     102    101
1 2016-12-31    952.150000   1761  104.0   105   104.0     104    104
2 2015-12-31    428.000000   2416  103.0   104   103.0     103    103
3 2014-12-31    317.400000   4115  102.0   101   102.0     102    102
4 2013-12-31    731.000000   2220  103.0   104   103.0     103    103
5 2012-12-31     13.590000     70  134.5   104   134.5     137    132
6 2011-12-31      4.995000     64  144.5   113   144.5     145    144
7 2010-12-31      0.299999      1  180.0   180   180.0     180    180
8 2009-12-31      0.000000      0   -1.0    -1    -1.0      -1     -1
>>> plot_graph(df, 'Bitcoin worth in USD', 'Price of Bitcoin from 1/1/2009 to 12/1/2017')
plot_graph(df, 'Bitcoin worth in USD', 'Price of Bitcoin from 1/1/2009 to 12/1/2017')
</pre>

# Data Sources

Quandl - https://www.quandl.com/search

Reddit - https://www.reddit.com/r/redditdev/comments/64cs5u/new_pushshift_api_endpoint_all_reddit_submissions/