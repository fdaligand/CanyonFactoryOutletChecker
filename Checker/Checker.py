import requests
from Parser import *
import yaml
import pdb


class Checker(object):

    def __init__(self, config_file):
        self.params = self.loadConfig(config_file)
        self.config_path = config_file

    def loadConfig(self, config):
        # open file but when is it close
        return yaml.load(open(config, 'r'))

    def getPage(self):

        #TODO: add the possibility of overloading the requested url
        #req = requests.get("{mainUrl}".format(mainUrl=self.generalParameter.url),auth=(self.generalParameter.user,self.generalParameter.pwd),params=urlParam)
        #req = requests.get("https://www.canyon.com/fr/factory-outlet/ajax/articles.html?category=road&type=html")
        req = requests.get("{url}{ajaxUrl}".format(url=self.params['mainUrl'],ajaxUrl=self.params['ajaxUrl']),params=self.params['urlParam'])
        return req.text
