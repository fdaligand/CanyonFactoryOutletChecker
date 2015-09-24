from Parameter import SpecificParameter as SP
from Parser import CanyonParser as CP
import pdb

params = SP.SpecificParameter(r"https://www.canyon.com/en-fr/factory-outlet",config=r"C:\Users\fdalingand\GitHub\CanyonFactoryOutlet\Config\canyon.cfg")
parser = CP.CanyonParser(params.configPath)
pdb.set_trace()
