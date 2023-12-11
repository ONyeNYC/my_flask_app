from peewee import Model, SqliteDatabase, CharField

# Initialize the database here directly
database = SqliteDatabase('my_database.db')

class BaseModel(Model):
    class Meta:
        database = database

class Item(BaseModel):
    name = CharField()

def initialize_db():
    database.connect()
    database.create_tables([Item], safe=True)
    database.close()
