class Parser(object):

    def __init__(self,event_dispatcher=None):
        
        self.event_dispatcher = event_dispatcher   

    def parseConfig(self,*args,**kwargs):
        """ base method to define where config file is parsed """
        pass

    def parseWebPage(self,*args,**kwargs):
        """ Base method to define where web page is parsed """
        pass
    def parseListOfParam(self,text):
        """ return a dict of a string of type key1=value1,key2=value2,...,keyN=valueN"""

        x = {}

        for keyValueCouple in text.split(",") :

            lstKeyValue = keyValueCouple.split('=')
            if len(lstKeyValue) == 2 :
                x[lstKeyValue[0]] = lstKeyValue[1]
            else:
                #TODO: raise an error of formating
                print "Error : Bad formating!"

        return x

    def raiseEvent(self,tup):
        return tup[0]
	




