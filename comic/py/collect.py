import os
import json
from db import db, DATABASE, Comic, Episode, Page


def readJsonFile(fileList):
    fileDict = {}
    for i in fileList:
        with open('../source/'+i, 'rb') as f:
            comic = f.read()
            comic = comic.decode()
            comic = json.loads(comic)
            fileDict[i] = comic
    return fileDict


def updateComic(comic, fileName):
    comicObj = Comic.returnComic(comic.get('编号'))
    if not comicObj:
        comicObj = Comic.createComic(comic.get('编号'), comic.get('名称'), comic.get('作者'))
    contributor = fileName[:fileName.rindex('.')]
    updateEpisode(comic, comicObj, contributor)


def updateEpisode(comic, comicObj, contributor):
    vols = comic.get('卷')
    episodes = comic.get('话')
    specials = comic.get('番外')
    if vols:
        for vol, pages in vols.items():
            episodeObj = Episode.returnEpisode(comicObj, vol=vol)
            if not episodeObj:
                episodeObj = Episode.createEpisode(comicObj, contributor, vol=vol)
            updatePage(episodeObj, pages)
    if episodes:
        for episode, pages in episodes.items():
            episodeObj = Episode.returnEpisode(comicObj, episode=episode)
            if not episodeObj:
                episodeObj = Episode.createEpisode(comicObj, contributor, episode=episode)
            updatePage(episodeObj, pages)
    if specials:
        for special, pages in specials.items():
            episodeObj = Episode.returnEpisode(comicObj, special=special)
            if not episodeObj:
                episodeObj = Episode.createEpisode(comicObj, contributor, special=special)
            updatePage(episodeObj, pages)


def updatePage(episodeObj, pages):
    for index, value in enumerate(pages):
        Page.create(episode=episodeObj, page=index+1, url=value)


def insertDataBase(fileDict):
    for fileName, value in fileDict.items():
        for comic in value:
            updateComic(comic, fileName)


def initDatabase():
    db.connect()
    db.create_tables([Comic, Episode, Page])
    db.close()


def main():
    if not os.path.isfile(DATABASE):
        initDatabase()
    assert 'source' in os.listdir('..'), 'comic下不存在source文件夹'
    fileList = os.listdir(os.path.join('..', 'source'))
    fileDict = readJsonFile(fileList)
    insertDataBase(fileDict)


if __name__ == '__main__':
    main()