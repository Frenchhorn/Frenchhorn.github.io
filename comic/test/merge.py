import os.path, datetime
import peewee

DATABASE = 'source.db'

db = peewee.SqliteDatabase(DATABASE)

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Comic(BaseModel):
    comicID = peewee.IntegerField(unique=True)
    name = peewee.CharField()
    author = peewee.CharField(default='unknown')
    location = peewee.CharField(default='unknown')
    finished = peewee.BooleanField(default=False)

    @staticmethod
    def searchByName(name):
        return Comic.select().where(Comic.name.contains(name))

    @staticmethod
    def searchByAuthor(author):
        return Comic.select().where(Comic.author.contains(author))
    
    @staticmethod
    def searchByLocation(location):
        return Comic.select().where(Comic.location.contains(location))
    
    @staticmethod
    def searchByAll(word):
        return Comic.select().where(Comic.name.contains(word) |
                                    Comic.author.contains(word) |
                                    Comic.location.contains(word))

class Episode(BaseModel):
    comic = peewee.ForeignKeyField(Comic, related_name='comic_episode')
    vol = peewee.IntegerField(null=True)
    episode = peewee.FloatField(null=True)
    contributor = peewee.CharField()
    date = peewee.DateTimeField(default=datetime.datetime.now())

class Page(BaseModel):
    episode = peewee.ForeignKeyField(Episode, related_name='episode_page')
    page = peewee.IntegerField()
    url = peewee.CharField()

class File(BaseModel):
    name = peewee.CharField(unique=True)
    date = peewee.DateTimeField()
    
    @staticmethod
    def getFileDate(name):
        try:
            fileDate = File.select().where(File.name == name).get()
            fileDate = fileDate.date.timestamp()
            return fileDate
        except:
            return False


def initDatabase():
    db.connect()
    db.create_tables([Comic, Episode, Page, File])
    db.close()


def validFileTime(fileList):
    newFileList = []
    for file in fileList:
        fileDate = File.getFileDate(file)
        if not fileDate or fileDate == os.path.getmtime('source/'+file):
            continue
        newFileList.append(file)
    return newFileList

def validFile(fileList):
    pass

def insertDataBase(fileList):
    pass

def test():
    Comic.create(comicID=1, name='1')
    Comic.create(comicID=2, name='12')
    c = Comic.create(comicID=3, name='123')
    Episode.create(comic=c, contributor='test')
    File.create(name='t', date=datetime.datetime.now())

def main():
    if not os.path.isfile(DATABASE):
        initDatabase()
    db.connect()
    
    try:
        fileList = os.listdir('source')
    except:
        print("Can't find folder source")
        db.close()
        return False
    
    fileList = validFileTime(fileList)
    fileList = validFile(fileList)
    insertDataBase(fileList)

if __name__ == '__main__':
    main()
