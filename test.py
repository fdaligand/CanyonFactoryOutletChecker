from Parser.CanyonParser import CanyonParser
from Checker.Checker import Checker
from Dispatcher.EventDispatcher import EventDispatcher
from Formater.Format import CanyonFormat,Email
import os
import pdb

BASE_DIR = os.getcwd()
EP = EventDispatcher()

# To be remove as CanyonFormat object also parse the config file
check = Checker(BASE_DIR+'/Config/canyon.yaml')

# CanyonFormat don't load the full config but only the filter part, load config in two place is bad, to be refactored
formater = CanyonFormat(eventDispatcher=EP,config=BASE_DIR+'/Config/canyon.yaml')
parser = CanyonParser(eventDispatcher=EP)

parser.parseWebPage(check.getPage())
email=Email(config=BASE_DIR+'/Config/canyon.yaml',msg=formater)
email.send()
