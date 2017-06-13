import os
import json
import db


def readJsonFile(fileList, fileFolder):
    fileDict = {}
    for fileName in fileList:
        filePath = os.path.join(fileFolder,fileName)
        with open(filePath, 'rb') as f:
            comic = f.read()
            comic = comic.decode()
            comic = json.loads(comic)
            fileDict[fileName] = comic
    return fileDict


def insertDataBase(fileDict):
    for fileName, value in fileDict.items():
        for comic in value:
            db.updateComic(comic)


def main():
    if not os.path.isfile(db.DATABASE):
        db.initDatabase()
    assert 'collect' in os.listdir('..'), 'comic下不存在collect文件夹'
    fileFolder = os.path.join('..', 'collect')
    fileList = os.listdir(fileFolder)
    fileDict = readJsonFile(fileList, fileFolder)
    insertDataBase(fileDict)


if __name__ == '__main__':
    main()