from peewee import *
import os

class Database:

    DB_PATH = os.path.join(os.path.dirname(__file__), "CFO_2.db")
    def __init__(self):
        """ Create or load existing databse"""
        if not os.path.isfile(self.DB_PATH):
            pass
        self.db = SqliteDatabase(self.DB_PATH)


def create_tables():
    db.connect()
    db.create_tables([Category, SubCategory, Serie, Item])

class BaseModel(Model):
    class Meta:
        database = Database().db

class Category(BaseModel):

    name = CharField(max_length=255)

class SubCategory(BaseModel):

    name = CharField(max_length=255)
    category = ForeignKeyField(Category)

class Serie(BaseModel):

    name = CharField(max_length=255)
    subCategory = ForeignKeyField(SubCategory)


class Item(BaseModel):

    item_id = CharField(max_length=255,primary_key=True)
    price = IntegerField()
    diff = IntegerField()
    date = CharField(max_length=255)
    size = CharField(max_length=255)
    state = CharField(max_length=255)
    year = IntegerField()
    url = CharField(max_length=255)
    serie = ForeignKeyField(Serie)

    def getSerie(self):

        return Serie.get(Serie.id == self.serie_id).name




# Exemple of creation on unique constraint
#class Attribut(BaseModel):
#
#    key = CharField(max_length=255)
#    value = CharField(max_length=255)
#
#    class Meta:
#        indexes=((('key','value'),True),
#                )


if __name__ == '__main__' :

    from ORM import *
    import pdb

    pdb.set_trace()

    print Category.get(Category.id == 1)


