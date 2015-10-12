from Parser import Parser
import ConfigParser
from lxml import html
from DB import ORM
from DB.ORM import Category,SubCategory,Item,AttribToItem,Attribut
import peewee
import pdb

class CanyonParser(Parser):

    def __init__(self,configPath=None):

        self.params = CanyonParser.parseConfig(self,configPath)
        self.webParams = {}
        pass

    def parseConfig(self,configPath):
        """ Parse specific cfg file """
        params={}

        if configPath:
            cfg =  ConfigParser.ConfigParser()
            cfg.read(configPath)
            if cfg.has_section('WebParam'):
                params['specificUrlLink'] = cfg.get('WebParam','specificUrlLink')
                params['urlParameter']=self.parseListOfParam(cfg.get('WebParam','paramsOnUrl'))

        else:
            print "No configuration file to parse"

        return params

    def parseWebPage(self,webText):

        foundModel = 0

        tree = html.fromstring(webText)
        #remove first ellement where is a dumy example

        #
        #
        #
        #
        #
        #
        #

        elements = tree.getchildren()[1:]

        for element in elements:

            #create a dict with all relevant information

            self.updateModels(element.attrib)
            if '|L|' in element.attrib.get('data-size',None):

                foundModel += 1
                print "I found a new bicycle named %s"%element.attrib.get('data-series','unknow')
                print " It's the %d found model"%foundModel

        return self.webParams

    def updateModels(self,parsedData):

        #find category and subcategory
        if (parsedData.get('data-category')) :

            cateAndSubCate = [x for x in parsedData.get('data-category').split('|') if x != '' ]
            cate,isCreated = Category.get_or_create(name=cateAndSubCate[0])
            print "category : %s"%cate.name
            subCate,dummy = SubCategory.get_or_create(name=cateAndSubCate[1],category=cate.id)
            print "sub-category : %s"%subCate.name

            if (parsedData.get('data-series')):
                serie,dummy = Item.get_or_create(name=parsedData['data-series'],subCategory=subCate.id)
                print "item: %s"%serie.name
            else :
               return

           #parse all parameters
            for key,value in parsedData.items():

                if key in ['data-category','data-series']:
                    continue

                atrib,dummy = Attribut.get_or_create(key=key,value=value)
                print "Atribut : %s = %s"%(atrib.key,atrib.value)
                atribToItem,dummy = AttribToItem.get_or_create(item = serie.id , attribut = atrib.id )






        else :
            raise NameError("No category/subcategory found, check html syntaxe!")

if __name__ == '__main__':

    testParser = CanyonParser()
    dummyWebPage = ""
    with open(r'..\DumpHtmlPage\test.html','r') as inputFile:
        for line in inputFile:
            dummyWebPage += line
    retFromParser = testParser.parseWebPage(dummyWebPage)
