import os
import datetime
import json
import db

COLLECT_FOLDER = os.path.join('..', 'collect')
TODAY_FOLDER = os.path.join(COLLECT_FOLDER, 'done', datetime.datetime.now().strftime('%Y%m%d'))


def readJsonFile(fileList):
    fileDict = {}
    for fileName in fileList:
        filePath = os.path.join(COLLECT_FOLDER,fileName)
        with open(filePath, 'rb') as f:
            print('Read file %s' % filePath)
            comic = f.read()
            comic = comic.decode()
            comic = json.loads(comic)
            fileDict[fileName] = comic
    return fileDict


def insertToDataBase(fileDict):
    for fileName, value in fileDict.items():
        for comic in value:
            db.updateComic(comic)
        # 移动已处理的文件到相应的文件夹
        print('Move file %s' % fileName)
        os.rename(os.path.join(COLLECT_FOLDER,fileName), os.path.join(TODAY_FOLDER,fileName))


def main():
    if not os.path.isfile(db.DATABASE):
        db.initDatabase()
    assert os.path.isdir(COLLECT_FOLDER), 'comic下不存在collect文件夹'
    if not os.path.isdir(TODAY_FOLDER):
        # 创建文件夹用于今次处理的文件
        os.mkdir(TODAY_FOLDER)
    fileList = filter(lambda x: x != 'done', os.listdir(COLLECT_FOLDER))
    fileDict = readJsonFile(fileList)
    insertToDataBase(fileDict)
    if len(os.listdir(TODAY_FOLDER)) == 0:
        # 删除空文件夹
        os.rmdir(TODAY_FOLDER)


if __name__ == '__main__':
    main()