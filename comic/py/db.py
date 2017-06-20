import os.path
import peewee
from collections import OrderedDict

DATABASE = os.path.join('..', 'comic.db')

db = peewee.SqliteDatabase(DATABASE)


# define tables
class BaseModel(peewee.Model):
    class Meta:
        database = db


class Comic(BaseModel):
    comicID = peewee.IntegerField(unique=True)
    name = peewee.CharField()
    author = peewee.CharField(null=True)


class Episode(BaseModel):
    comic = peewee.ForeignKeyField(Comic, related_name='comic_episode')
    vol = peewee.IntegerField(null=True)
    episode = peewee.FloatField(null=True)
    special = peewee.CharField(null=True)


class Page(BaseModel):
    episode = peewee.ForeignKeyField(Episode, related_name='episode_page')
    page = peewee.IntegerField()
    url = peewee.CharField()


# for collect.py
def updateComic(comic):
    query = Comic.select().where(Comic.comicID == comic.get('编号'))
    comicObj = query.get() if (len(query) != 0) else Comic.create(comicID=comic.get('编号'), name=comic.get('名称'), author=comic.get('作者'))
    updateEpisode(comic, comicObj)


def updateEpisode(comic, comicObj):
    vols = comic.get('卷')
    episodes = comic.get('话')
    specials = comic.get('番外')
    for index, itemDict in enumerate([vols, episodes, specials]):
        if not itemDict:
            continue
        for item, pages in itemDict.items():
            if index == 0:
                vol = int(item)
                # query = Episode.select().where((Episode.comic==comicObj) & (Episode.vol==vol))
                # episodeObj = query.get() if (len(query) != 0) else Episode.create(comic=comicObj, vol=vol)
                episodeObj = Episode.create(comic=comicObj, vol=vol)
            elif index == 1:
                episode = float(item)
                # query = Episode.select().where((Episode.comic==comicObj) & (Episode.episode==episode))
                # episodeObj = query.get() if (len(query) != 0) else Episode.create(comic=comicObj, episode=episode)
                episodeObj = Episode.create(comic=comicObj, episode=episode)
            elif index == 2:
                special = str(item)
                # query = Episode.select().where((Episode.comic==comicObj) & (Episode.special==special))
                # episodeObj = query.get() if (len(query) != 0) else Episode.create(comic=comicObj, special=special)
                episodeObj = Episode.create(comic=comicObj, special=special)

            updatePage(episodeObj, pages)


def updatePage(episodeObj, pages):
    for index, value in enumerate(pages):
        Page.create(episode=episodeObj, page=index+1, url=value)


# for generate.py
def getIndex():
    index = []
    comicIterator = Comic.select().order_by(Comic.comicID)
    for comicObj in comicIterator:
        comicIndex = OrderedDict()
        comicIndex['编号'] = comicObj.comicID
        comicIndex['名称'] = comicObj.name
        comicIndex['作者'] = comicObj.author
        comicIndex['卷'] = len(Episode.select().where((Episode.comic==comicObj) & (Episode.vol != None)))
        comicIndex['话'] = len(Episode.select().where((Episode.comic==comicObj) & (Episode.episode != None)))
        comicIndex['番外'] = len(Episode.select().where((Episode.comic==comicObj) & (Episode.special != None)))
        index.append(comicIndex)
    return index


def getComic(comic):
    comic['卷'] = OrderedDict()
    comic['话'] = OrderedDict()
    comic['番外'] = OrderedDict()
    comicObj = Comic.get(comicID=comic['编号'])
    episodeIterator = Episode.select().where(Episode.comic==comicObj).order_by(Episode.special, Episode.episode, Episode.vol)
    for episodeObj in episodeIterator:
        if episodeObj.vol:
            if not comic['卷'].get(episodeObj.vol):
                comic['卷'][episodeObj.vol] = []
            pageList = []
            pageObjs = Page.select().where(Page.episode==episodeObj).order_by(Page.page)
            for pageObj in pageObjs:
                pageList.append(pageObj.url)
            comic['卷'][episodeObj.vol].append(pageList)
        elif episodeObj.episode:
            if not comic['话'].get(episodeObj.episode):
                comic['话'][episodeObj.episode] = []
            pageList = []
            pageObjs = Page.select().where(Page.episode==episodeObj).order_by(Page.page)
            for pageObj in pageObjs:
                pageList.append(pageObj.url)
            comic['话'][episodeObj.episode].append(pageList)
        elif episodeObj.special:
            if not comic['番外'].get(episodeObj.special):
                comic['番外'][episodeObj.special] = []
            pageList = []
            pageObjs = Page.select().where(Page.episode==episodeObj).order_by(Page.page)
            for pageObj in pageObjs:
                pageList.append(pageObj.url)
            comic['番外'][episodeObj.special].append(pageList)
    return comic


# create database
def initDatabase():
    db.connect()
    db.create_tables([Comic, Episode, Page])
    db.close()


# simple test
def test():
    Comic.create(comicID=1, name='东方铃奈庵', author='春河もえ/zun')
    Comic.create(comicID=2, name='四叶妹妹')
    comic3 = Comic.create(comicID=3, name='迷你偶像', author='明音')
    vol1 = Episode.create(comic=comic3, vol=1)
    Episode.create(comic=comic3, episode=1.5)
    Episode.create(comic=comic3, special='1.5')
    Page.create(episode=vol1, page=1, url='迷你偶像 卷1 页1')


if __name__ == '__main__':
    if not os.path.isfile(DATABASE):
        initDatabase()
