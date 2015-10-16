import requests
from Parser import *
import pdb

class Checker(object):

    def __init__(self,params):
        self.generalParameter = params

    def go(self):

        urlParam = 'category=road,type=html'
        #TODO: add the possibility of overloading the requested url
        #req = requests.get("{mainUrl}".format(mainUrl=self.generalParameter.url),auth=(self.generalParameter.user,self.generalParameter.pwd),params=urlParam)
        req = requests.get("https://www.canyon.com/fr/factory-outlet/ajax/articles.html?category=road&type=html")
        return req.text
