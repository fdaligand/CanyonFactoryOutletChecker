import requests
from Parser import *
import pdb

class Checker(object):

    def __init__(self,parser,params):
        self.parsedResult = {}
        self.parser = parser
        self.generalParameter = params

        pass

    def go(self):

        urlParam = self.parser.params['urlParameter']
        #TODO: add the possibility of overloading the requested url
        req = requests.get("{mainUrl}".format(mainUrl=self.generalParameter.url),auth=(self.generalParameter.user,self.generalParameter.pwd),params=urlParam)
        self.parsedResult = self.parser.parseWebPage(req.text)
        pdb.set_trace()
        return "Checker ended"
