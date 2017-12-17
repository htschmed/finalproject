import requests
from data import DataModel

class RedditModel(DataModel):

    def __init__(self):
        DataModel.__init__(self, 'REDDIT')

    def getArticleCount(self, start_time, end_time, subject):
        params = {}
        query = '(title:{} AND created_utc:>{} AND created_utc:<{})'\
                    .format(
                            subject,
                            start_time.strftime('%s'),
                            end_time.strftime('%s'),
                            )
        params['q'] = query
        params['sort'] = 'score'
        params['size'] = '100'
        r = requests.get(
            self.api_url,
            params=params
        )
        response = r.json()
        return response
        #return response['hits']['total']