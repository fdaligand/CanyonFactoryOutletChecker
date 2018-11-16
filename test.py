from Parser.CanyonParser import CanyonParser
from Checker.Checker import Checker
from Dispatcher.EventDispatcher import EventDispatcher
from Formater.Format import CanyonFormat, Email
import os
import pdb

BASE_DIR = os.path.dirname(__file__)
EP = EventDispatcher()

check = Checker(BASE_DIR+'/Config/canyon.yaml')

formater = CanyonFormat(eventDispatcher=EP, config=check.config_path)
parser = CanyonParser(eventDispatcher=EP)

parser.parseWebPage(check.getPage())
email=Email(config=BASE_DIR+'/Config/canyon.yaml',msg=formater)
email.send()
