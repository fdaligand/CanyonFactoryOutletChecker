from Parser import Parser
import ConfigParser

class CanyonParser(Parser):

    def __init__(self,configPath=None):

        self.params = CanyonParser.ParseConfig(self,configPath)
        pass

    def ParseConfig(self,configPath):
        """ Parse specific cfg file """
        params={}

        if configPath:
            cfg =  ConfigParser.ConfigParser()
            cfg.read(configPath)

            if cfg.has_section('WebParam'):
                params['specificUrlLink'] = cfg.get('WebParam','specificUrlLink')


        else:
            print "No configuration file to parse"

        return params
