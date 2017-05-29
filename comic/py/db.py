import os.path
import datetime
import peewee

DATABASE = os.path.join('..', 'comic.db')

db = peewee.SqliteDatabase(DATABASE)


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Comic(BaseModel):
    comicID = peewee.IntegerField(unique=True)
    name = peewee.CharField()
    author = peewee.CharField(default='unknown')

    # @staticmethod
    # def searchByName(name):
    #     return Comic.select().where(Comic.name.contains(name))

    # @staticmethod
    # def searchByAuthor(author):
    #     return Comic.select().where(Comic.author.contains(author))

    # @staticmethod
    # def searchByLocation(location):
    #     return Comic.select().where(Comic.location.contains(location))

    # @staticmethod
    # def searchByAll(word):
    #     return Comic.select().where(Comic.name.contains(word) |
    #                                 Comic.author.contains(word) |
    #                                 Comic.location.contains(word))


class Episode(BaseModel):
    comic = peewee.ForeignKeyField(Comic, related_name='comic_episode')
    vol = peewee.IntegerField(null=True)
    episode = peewee.FloatField(null=True)
    special = peewee.CharField(null=True)
    # contributor = peewee.CharField()


class Page(BaseModel):
    episode = peewee.ForeignKeyField(Episode, related_name='episode_page')
    page = peewee.IntegerField()
    url = peewee.CharField()


def initDatabase():
    db.connect()
    db.create_tables([Comic, Episode, Page])
    db.close()


def test():
    Comic.create(comicID=1, name='1')
    Comic.create(comicID=2, name='12')
    c = Comic.create(comicID=3, name='123')
    Episode.create(comic=c, contributor='test')


if __name__ == '__main__':
    if not os.path.isfile(DATABASE):
        initDatabase()
