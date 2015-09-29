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

        foundModel = 0

        tree = html.fromstring(webText)
        #remove first ellement where is a dumy example
        elements = tree.getchildren()[1:]

        for element in elements:

            if '|L|' in element.attrib.get('data-size',None):

                pdb.set_trace()
                foundModel += 1
                print "I found a new bicycle named %s"%element.attrib.get('data-series','unknow')
                print " It's the %d found model"%foundModel

        return self.webParams
