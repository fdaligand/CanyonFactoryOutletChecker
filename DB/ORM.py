from peewee import *
import os

db = SqliteDatabase(r'C:\Users\fdalingand\GitHub\CanyonFactoryOutlet\DB\CFO.db')

def create_tables():
    db.connect()
    db.create_tables([Category,SubCategory,Item,Attribut,AttribToItem])

class BaseModel(Model):
    class Meta:
        database = db

class Category(BaseModel):

    name = CharField(max_length=255)

class SubCategory(BaseModel):

    name = CharField(max_length=255)
    category = ForeignKeyField(Category)

class Item(BaseModel):

    name = CharField(max_length=255)
    subCategory = ForeignKeyField(SubCategory)

class Attribut(BaseModel):

    key = CharField(max_length=255)
    value = CharField(max_length=255)

    class Meta:
        indexes=((('key','value'),True),
                )

class AttribToItem(BaseModel):

    item = ForeignKeyField(Item)
    attribut = ForeignKeyField(Attribut)






if __name__ == '__main__' :

    from ORM import *
    import pdb

    pdb.set_trace()

    print Category.get(Category.id == 1)

