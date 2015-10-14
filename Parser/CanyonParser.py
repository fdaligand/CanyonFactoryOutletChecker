from Parser import Parser
import ConfigParser
from lxml import html
from DB import ORM
from DB.ORM import Category,SubCategory,Item,AttribToItem,Attribut
import peewee
import os
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

        errorInUpdate = False

        tree = html.fromstring(webText)
        #remove first ellement where is a dumy example
        elements = tree.getchildren()[1:]

        for element in elements:

            #create a dict with all relevant information
            newField,errorInUpdate = self.updateModels(element.attrib)

            #We detect new field durin update
            if newField:
                pass

            #Some errors (not critical) appear during update
            if errorInUpdate:
                pass

        return self.webParams

    def updateModels(self,parsedData):

        #find category and subcategory
        if (parsedData.get('data-category')) :

            cateAndSubCate = [x for x in parsedData.get('data-category').split('|') if x != '' ]
            cate = self.raiseEvent(Category.get_or_create(name=cateAndSubCate[0]))
            print "category : %s"%cate.name
            subCate,dummy = SubCategory.get_or_create(name=cateAndSubCate[1],category=cate.id)
            print "sub-category : %s"%subCate.name

            if (parsedData.get('data-series')):
                serie,dummy = Item.get_or_create(name=parsedData['data-series'],subCategory=subCate.id)
                print "item: %s"%serie.name
            else :
               return None,True

           #parse all parameters
            for key,value in parsedData.items():

                #skip already parsed attributes
                if key in ['data-category','data-series']:
                    continue

                #atrib,dummy = Attribut.get_or_create(key=key,value=value)
                atrib,dummy = Attribut.get_or_create(key=key,value=value)
                #print "Atribut : %s = %s"%(atrib.key,atrib.value)
                atribToItem,dummy = AttribToItem.get_or_create(item = serie.id , attribut = atrib.id )

            return None,False
        else :
            return None,True

    def raiseEvent(self,tup):
	if tup[1]:
	    raise NameError("New update in database")
        else :
            return tup[0]


if __name__ == '__main__':

    testParser = CanyonParser()
    pathFile = os.path.join('..','DumpHtmlPage','test.html')
    dummyWebPage = ""
    with open(pathFile ,'r') as inputFile:
        for line in inputFile:
            dummyWebPage += line
    retFromParser = testParser.parseWebPage(dummyWebPage)
