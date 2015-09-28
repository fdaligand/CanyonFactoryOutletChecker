from Parameter import SpecificParameter as SP
from Parser import CanyonParser as CP
from Checker import Checker as CK

import pdb

params = SP.SpecificParameter(r"https://www.canyon.com/fr/factory-outlet/ajax/articles.html",config=r"C:\Users\fdalingand\GitHub\CanyonFactoryOutlet\Config\canyon.cfg")
parser = CP.CanyonParser(params.configPath)
check = CK.Checker(parser,params)
resp = check.go()
