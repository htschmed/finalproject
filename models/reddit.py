import requests
from .base_model import DataModel
from statistics import mean, median, mode, median_low, median_high, StatisticsError

class RedditModel(DataModel):

    def __init__(self):
        DataModel.__init__(self, 'REDDIT')

    def getArticleData(self, start_time, end_time, subject, min_score=-1, size=100):
        params = {}
        query = '(title:{} AND created_utc:>{} AND created_utc:<{} AND score:>{})'\
                        .format(
                            subject,
                            start_time.strftime('%s'),
                            end_time.strftime('%s'),
                            min_score
                            )
        params['q'] = query
        params['sort'] = 'score'
        params['size'] = size
        r = requests.get(
            self.api_url,
            params=params
        )
        response = r.json()

        scores = []
        for row in response['hits']['hits']:
            scores.append(row['_source']['score'])

        stats_result = {}
        stats_result['posts'] = response['hits']['total']
        try:
            stats_result['mean'] = mean(scores)
        except StatisticsError:
            stats_result['mean'] = -1
        try:
            stats_result['mode'] = mode(scores)
        except StatisticsError:
            stats_result['mode'] = -1
        try:
            stats_result['median'] = median(scores)
        except StatisticsError:
            stats_result['median'] = -1
        try:
            stats_result['m_high'] = median_high(scores)
        except StatisticsError:
            stats_result['m_high'] = -1
        try:
            stats_result['m_low'] = median_low(scores)
        except StatisticsError:
            stats_result['m_low'] = -1

        return stats_result