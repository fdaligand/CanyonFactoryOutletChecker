import requests

class Checker(object):

    def __init__(self):
        pass

    def go(self,parser,params):

        req = requests.get("{mainUrl}/#{linkUrl}".format(mainUrl=params.url,linkUrl=parser.params['specificUrlLink']),auth=(params.user,params.pwd))
        return req.status_code
