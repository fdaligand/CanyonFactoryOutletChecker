from Parameter.SpecificParameter import SpecificParameter
from Parser.CanyonParser import CanyonParser
from Checker.Checker import Checker
from Dispatcher.EventDispatcher import EventDispatcher
from Formater.Format import CanyonFormat

import pdb

EP = EventDispatcher()

params = SpecificParameter(r"https://www.canyon.com/fr/factory-outlet/ajax/articles.html",config=r"C:\Users\fdalingand\GitHub\CanyonFactoryOutlet\Config\canyon.cfg")
check = Checker(params)

formater = CanyonFormat(eventDispatcher=EP)
parser = CanyonParser(params.configPath,eventDispatcher=EP)

parser.parseWebPage(check.go())
pdb.set_trace()


