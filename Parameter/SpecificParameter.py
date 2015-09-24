from Parameter import Parameter
import ConfigParser

class SpecificParameter(Parameter):

    def __init__(self,url, user=None,pwd=None,config=None):

        Parameter.__init__(self,url,user,pwd)
        self.configPath = config



