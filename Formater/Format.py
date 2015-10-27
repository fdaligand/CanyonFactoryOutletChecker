from Dispatcher import Event
import yaml
import pdb
import smtplib
import getpass

class Format( object ):

    def __init__(self,config):

        self._text=""
        self._specificText=""
        self._filter=self._loadFilter(config)

    def _loadFilter(self,config):

        x = yaml.load(open(config,'r'))
        return x.get('filter',None)


class CanyonFormat(Format):

    def __init__(self,eventDispatcher,config):

        super(CanyonFormat,self).__init__(config)
        self._eventDispatcher=eventDispatcher
        self._eventDispatcher.addEventListener("Item", self.appendNewItem)


    def appendNewItem(self,event):

        filtredEvent = False
        if self._filter :
            for key,value in self._filter.items():
                if value in event._data._data.get(key,''):
                    filtredEvent = True

        if filtredEvent:

            self._specificText += """New item detected on page:
            Serie : {serie} from year {year} in size {size}\n
            State : {state}
            Old Price:{oldPrice} \n
            New Price:{newPrice} \n

            Difference:{diff} \n

            More info : {url}\n

            _____________________________________________________________________
            ---------------------------------------------------------------------
            '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            """.format(serie= event._data.getSerie(),
                      year= event._data.year,
                      size= event._data.size,
                      state= event._data.state,
                      oldPrice= self.formatPrice(event._data.price),
                      newPrice= self.getNewPrice(event._data),
                      diff= self.formatPrice(event._data.diff),
                      url= event._data.url)



    def getNewPrice(self,model):

        return self.formatPrice(model.price-model.diff)

    def formatPrice(self,price):

        return "%d euro"%(price/100)

    def getText(self):

        return self._text+self._specificText



class Email( object ):

    def __init__(self,config,msg=None):

        self._from = 'florent.daligand.dev@gmail.com'
        self._to = self.getMailList(config)
        self._pwd = getpass.getpass(prompt="Enter the password of SMTP server")
        if msg:
            self._msg = msg.getText()
        else :
            self._msg = "message de test de la class Email"

    def getMailList(self,config):

        conf = yaml.load(open(config,'r'))

        if conf.get('email',None):
            return conf['email']['to']

    def send(self):

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
	server.login('florent.daligand.dev@gmail.com',self._pwd)
        server.sendmail(self._from,self._to,self._msg)
        server.quit()


if __name__ == '__main__' :

    pdb.set_trace()		
    mail= Email('../Config/canyon.yaml')
    mail.send()
