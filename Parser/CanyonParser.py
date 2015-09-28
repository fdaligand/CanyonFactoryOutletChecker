from Parser import Parser
import ConfigParser
from lxml import html
import pdb

class CanyonParser(Parser):

    def __init__(self,configPath=None):

        self.params = CanyonParser.parseConfig(self,configPath)
        self.webParams = {}
        pass

    def parseConfig(self,configPath):
        """ Parse specific cfg file """
        params={}

        if configPath:
            cfg =  ConfigParser.ConfigParser()
            cfg.read(configPath)
            if cfg.has_section('WebParam'):
                params['specificUrlLink'] = cfg.get('WebParam','specificUrlLink')
                params['urlParameter']=self.parseListOfParam(cfg.get('WebParam','paramsOnUrl'))

        else:
            print "No configuration file to parse"

        return params

    def parseWebPage(self,webText):

        tree = html.fromstring(webText)
        pdb.set_trace()
        return self.webParams
