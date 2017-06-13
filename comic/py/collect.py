import os
import json
import db


def readJsonFile(fileList):
    fileDict = {}
    for i in fileList:
        with open('../source/'+i, 'rb') as f:
            comic = f.read()
            comic = comic.decode()
            comic = json.loads(comic)
            fileDict[i] = comic
    return fileDict


def insertDataBase(fileDict):
    for fileName, value in fileDict.items():
        for comic in value:
            db.updateComic(comic)


def main():
    if not os.path.isfile(db.DATABASE):
        db.initDatabase()
    assert 'source' in os.listdir('..'), 'comic下不存在source文件夹'
    fileList = os.listdir(os.path.join('..', 'source'))
    fileDict = readJsonFile(fileList)
    insertDataBase(fileDict)


if __name__ == '__main__':
    main()