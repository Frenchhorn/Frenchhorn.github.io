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
    author = peewee.CharField(null=True)

    @staticmethod
    def returnComic(comicID):
        comicID = int(comicID)
        query = Comic.select().where(Comic.comicID == comicID)
        if len(query) == 0:
            return None
        else:
            return query.get()

    @staticmethod
    def createComic(comicID, name, author):
        return Comic.create(comicID=comicID, name=name, author=author)

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
    contributor = peewee.CharField()

    @staticmethod
    def returnEpisode(comicObj, vol=None, episode=None, special=None):
        if vol:
            vol = int(vol)
            query = Episode.select().where(Episode.comic == comicObj & Episode.vol == vol)
        elif episode:
            episode = float(episode)
            query = Episode.select().where(Episode.comic == comicObj & Episode.episode == episode)
        elif special:
            query = Episode.select().where(Episode.comic == comicObj & Episode.special == special)

        if len(query) == 0:
            return None
        else:
            return query.get()

    @staticmethod
    def createEpisode(comicObj, contributor, vol=None, episode=None, special=None):
        if vol:
            vol = int(vol)
            return Episode.create(comic=comicObj, contributor=contributor, vol=vol)
        elif episode:
            episode = float(episode)
            return Episode.create(comic=comicObj, contributor=contributor, episode=episode)
        elif special:
            return Episode.create(comic=comicObj, contributor=contributor, special=special)


class Page(BaseModel):
    episode = peewee.ForeignKeyField(Episode, related_name='episode_page')
    page = peewee.IntegerField()
    url = peewee.CharField()


def initDatabase():
    db.connect()
    db.create_tables([Comic, Episode, Page])
    db.close()


def test():
    Comic.create(comicID=1, name='东方铃奈庵', author='春河もえ/zun')
    Comic.create(comicID=2, name='四叶妹妹')
    comic3 = Comic.create(comicID=3, name='迷你偶像', author='明音')
    vol1 = Episode.create(comic=comic3, vol=1, contributor='kosuzu')
    Episode.create(comic=comic3, episode=1.5, contributor='kosuzu')
    Episode.create(comic=comic3, special='1.5', contributor='kosuzu')
    Page.create(episode=vol1, page=1, url='迷你偶像 卷1 页1')


if __name__ == '__main__':
    if not os.path.isfile(DATABASE):
        initDatabase()
