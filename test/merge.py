import peewee

DATABASE = 'source.db'

db = peewee.SqliteDatabase(DATABASE)

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Comic(peewee.Model):
    comicID = peewee.CharField(unique=True)
    

class Episode(BaseModel):
    comic = peewee.ForeignKeyField(Comic, related_name='comic_episode')
    vol = peewee.IntegerField()
    episode = peewee.FloatField()
    
    
class Page(BaseModel):
    episode = peewee.ForeignKeyField(Episode, related_name='episode_page')
    page = peewee.IntegerField()
        
def initDatabase():
    db.connect()
    db.create_tables([Index])