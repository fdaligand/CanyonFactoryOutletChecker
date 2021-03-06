from Parser import Parser
import ConfigParser
from lxml import html
from DB import ORM
from DB.ORM import Category,SubCategory,Serie,Item
from Dispatcher.EventDispatcher import EventDispatcher
from Dispatcher.Event import DbEvent
from Formater.Format import CanyonFormat
import peewee
import os
import pdb


class CanyonParser(Parser):

    def __init__(self, configPath=None, eventDispatcher=None):

        self.params = CanyonParser.parseConfig(self, configPath)
        self.webParams = {}
        self.eventDispatcher = eventDispatcher


    def parseConfig(self, configPath):
        """ Parse specific cfg file """
        pass

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

    def updateModels(self, parsed_data):

        #find category and subcategory
        if (parsed_data.get('data-category')) :

            cateAndSubCate = [x for x in parsed_data.get('data-category').split('|') if x != '']
            cate = self.raiseEvent(Category.get_or_create(name=cateAndSubCate[0]))
            print "category : %s"%cate.name
            subCate,dummy = SubCategory.get_or_create(name=cateAndSubCate[1],category=cate.id)
            print "   *sub-category : %s"%subCate.name

            if (parsed_data.get('data-series')):
                serie,dummy = Serie.get_or_create(name=parsed_data['data-series'], subCategory=subCate.id)
                print "        -Serie: %s"%serie.name
            else :
               return None,True

            if parsed_data.get('data-id'):
                try:
                    item = Item.get(Item.item_id == parsed_data['data-id'])
                except peewee.DoesNotExist :
                    item = Item.create(item_id=parsed_data['data-id'],
                                       price=int(parsed_data.get('data-price', '0')),
                                       diff=int(parsed_data.get('data-diff', '0')),
                                       date=parsed_data.get('data-date', 'No date'),
                                       size=parsed_data.get('data-size', 'No size'),
                                       state=parsed_data.get('data-state', 'No state'),
                                       year=int(parsed_data.get('data-year', '0')),
                                       url=parsed_data.get('data-url', 'No url'),
                                       serie=serie.id)
                    self.eventDispatcher.dispatchEvent(DbEvent(item.__class__.__name__, item.id, data=item))


            return None,False
        else :
            return None,True

    def raiseEvent(self,tup):

        if tup[1]:
            self.eventDispatcher.dispatchEvent( DbEvent(tup[0].__class__.__name__,tup[0].id,data=tup[0] ))
            return tup[0]

        else :
            return tup[0]


if __name__ == '__main__':

    EP = EventDispatcher()
    formater = CanyonFormat(eventDispatcher=EP)
    #TODO try with dynamic instanciation
    testParser = CanyonParser(eventDispatcher=EP)
    pathFile = os.path.join('..','DumpHtmlPage','test.html')
    dummyWebPage = ""
    with open(pathFile ,'r') as inputFile:
        for line in inputFile:
            dummyWebPage += line
    retFromParser = testParser.parseWebPage(dummyWebPage)
