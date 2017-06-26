import os
import json
import db

COLLECT_FOLDER = os.path.join('..', 'collect')

def readJsonFile(fileList):
    fileDict = {}
    for fileName in fileList:
        filePath = os.path.join(COLLECT_FOLDER,fileName)
        with open(filePath, 'rb') as f:
            comic = f.read()
            comic = comic.decode()
            comic = json.loads(comic)
            fileDict[fileName] = comic
    return fileDict


def insertToDataBase(fileDict):
    for fileName, value in fileDict.items():
        for comic in value:
            db.updateComic(comic)


def main():
    if not os.path.isfile(db.DATABASE):
        db.initDatabase()
    assert os.path.isdir(COLLECT_FOLDER), 'comic下不存在collect文件夹'
    fileList = os.listdir(COLLECT_FOLDER)
    fileDict = readJsonFile(fileList)
    insertToDataBase(fileDict)


if __name__ == '__main__':
    main()