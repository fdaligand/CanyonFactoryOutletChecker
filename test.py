from Parser.CanyonParser import CanyonParser
from Checker.Checker import Checker
from Dispatcher.EventDispatcher import EventDispatcher
from Formater.Format import CanyonFormat,Email
import os


CONFIG_PATH = os.path.join(os.getcwd(), 'Config', 'canyon.yaml')
EP = EventDispatcher()

check = Checker(CONFIG_PATH)

formater = CanyonFormat(eventDispatcher=EP, config=CONFIG_PATH)
parser = CanyonParser(eventDispatcher=EP)

parser.parseWebPage(check.getPage())
email = Email(config=CONFIG_PATH, msg=formater)
email.send()
