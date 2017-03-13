import requests
from Parser import *
import yaml

class Checker(object):

    def __init__(self,configFile):
        self.params = self.loadConfig(configFile)

    def loadConfig(self,config):
        return yaml.load(open(config,'r'))

    def getPage(self):

        #TODO: add the possibility of overloading the requested url
        #req = requests.get("{mainUrl}".format(mainUrl=self.generalParameter.url),auth=(self.generalParameter.user,self.generalParameter.pwd),params=urlParam)
        #req = requests.get("https://www.canyon.com/fr/factory-outlet/ajax/articles.html?category=road&type=html")
        req = requests.get("{url}{ajaxUrl}".format(url=self.params['mainUrl'],ajaxUrl=self.params['ajaxUrl']),params=self.params['urlParam'])
        return req.text
