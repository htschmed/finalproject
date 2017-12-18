# Installation
Requires Python 3.5 or greater. Install packages using the following command after cloning the repo:

`pip install -r requirements.txt`

A configuration file called *config.ini* is also required in the root directory.  See the example ini file for settings

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