import configparser

class DataModel:

    def __init__(self, section):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.api_url = config[section]['api_url']
        if 'api_key' in config[section].keys():
            self.api_key = config[section]['api_key']

