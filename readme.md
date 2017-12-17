# Installation
Requires Python 3.5 or greater. Install packages using the following command after cloning the repo:

`pip install -r requirements.txt`

A configuration file called *config.ini* is also required in the root directory.  See the example ini file for settings

# Sample Usage
Finance
<pre>
>>> from finance import DataModel
from finance import FinanceModel
>>> test = FinanceModel()
test = DataModel()
>>> test.show_graph('BCHAIN/ATRCT', {'collapse': 'quarterly', 'start_date': '2013-01-01', 'end_date': '2015-12-31'}, 'Wait time in minutes')
test.show_graph('BCHAIN/ATRCT', {'collapse': 'quarterly', 'start_date': '2013-01-01', 'end_date': '2015-12-31'}, 'Wait time in minutes')
>>> test.show_graph('BCHAIN/DIFF', {'collapse': 'quarterly', 'start_date': '2013-01-01', 'end_date': '2015-12-31'}, 'Difficulty')
test.show_graph('BCHAIN/DIFF', {'collapse': 'quarterly', 'start_date': '2013-01-01', 'end_date': '2015-12-31'}, 'Difficulty')
</pre>

Reddit
<pre>
>>> import datetime
import datetime
>>> from reddit import RedditModel
from reddit import RedditModel
>>> test = RedditModel()
test = RedditModel()
>>> startdate = datetime.date(2015,1,1)
startdate = datetime.date(2015,1,1)
>>> enddate = datetime.date(2016,1,1)
enddate = datetime.date(2016,1,1)
>>> r = test.getArticleCount(startdate,enddate,'bitcoin')
r = test.getArticleCount(startdate,enddate,'bitcoin')
>>> r['hits']['total']
r['hits']['total']
116294
>>> 
</pre>