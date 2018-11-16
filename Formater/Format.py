
import yaml
import smtplib
import getpass

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Format(object):

    def __init__(self, config):

        self._text = ""
        self._html = ""
        self._specificText = ""
        self._filter = self._loadFilter(config)

    def _loadFilter(self, config):

        x = yaml.load(open(config, 'r'))
        return x.get('filter', None)

    def _toHtml(self):
        pass
	
    def _filtering(self, data):
	
        filtredEvent = False
	if self._filter :
	    for key, value in self._filter.items():
		if value in data.__getattribute__(key):
		    filtredEvent = True
        
        return filtredEvent


	

class CanyonFormat(Format):

    def __init__(self,eventDispatcher,config):

        super(CanyonFormat, self).__init__(config)
        self._eventDispatcher=eventDispatcher
        self._eventDispatcher.addEventListener("Item", self.appendNewItem)
        self._eventDispatcher.addEventListener("Item", self._toHtml)

    
    def _toHtml(self,event):
        """ append new item from event in html format"""
        if self._filtering(event._data):
	        self._html += """ <br/>
				<br/>		
				<h1> New Item on canyon Factory Outlet </h1>
				<br/>
				<br/>
				<h2> Model {serie}</h2>
				<p> Size {size}
				<h3><strong> {newPrice} Euros</strong> ( - {diff} Euros )</h3>
				<br/>
				<br/>""".format(serie= event._data.getSerie(),
                      				size= event._data.size,
                      				newPrice=self.formatPrice(event._data.price),
                      				diff=self.formatPrice(event._data.diff)
						)

        	
    def appendNewItem(self,event):

        if self._filtering(event._data):

            self._specificText += """New item detected on the Factory Outlet
            
            Serie : {serie} from year {year} in size {size}\n
            State : {state}
            Price:{newPrice} \n
            Old Price:{oldPrice} \n

            Difference:{diff} \n

            More info : {url}\n

            _____________________________________________________________________
            ---------------------------------------------------------------------
            '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            """.format(serie= event._data.getSerie(),
                      year= event._data.year,
                      size= event._data.size,
                      state= event._data.state,
                      oldPrice=self.getOldPrice(event._data),
                      newPrice=self.formatPrice(event._data.price),
                      diff= self.formatPrice(event._data.diff),
                      url= event._data.url)



    def getOldPrice(self,model):

        return self.formatPrice(model.price+model.diff)

    def formatPrice(self,price):

        return "%d euro"%(price/100)

    def getText(self):

        return self._text+self._specificText

    def getHtml(self):

        return self._html




class Email( object ):

    def __init__(self,config,msg=None):

        
	self._msg = MIMEMultipart('alternative')
	self._msg['Subject'] = "New Item on Canyon Factory Outlet"
	self._msg['From'] = 'florent.daligand.dev@gmail.com'
	self._msg['To'] = self.getMailList(config)
	
        self._pwd = getpass.getpass(prompt="Enter the password of SMTP server")
        
	if msg:
            self._text = msg.getText()
            self._html = msg.getHtml()
        else :
            self._text = "message de test de la class Email"
            self._html = "<h1>message de test de la class <strong>Email</strong></h1>"

	part1 = MIMEText(self._text,'plain')
	part2 = MIMEText(self._html,'html')

	self._msg.attach(part1)
	self._msg.attach(part2)

    def getMailList(self,config):

        conf = yaml.load(open(config,'r'))

        if conf.get('email',None):
            return conf['email']['to']

    def send(self):

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
	server.login('florent.daligand.dev@gmail.com',self._pwd)
	pdb.set_trace()
        server.sendmail(self._msg['From'],self._msg['To'],self._msg.as_string())
        server.quit()


if __name__ == '__main__' :

    mail= Email('../Config/canyon.yaml')
    mail.send()
