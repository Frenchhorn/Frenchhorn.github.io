import os
import datetime
import json
import db
from db import logger

COLLECT_FOLDER = os.path.join('..', 'collect')
TODAY_FOLDER = os.path.join(COLLECT_FOLDER, 'done', datetime.datetime.now().strftime('%Y%m%d'))


def readJsonFile(fileList):
    fileDict = {}
    for fileName in fileList:
        filePath = os.path.join(COLLECT_FOLDER,fileName)
        with open(filePath, 'rb') as f:
            logger.info('读取文件 %s' % filePath)
            comic = f.read()
            comic = comic.decode()
            comic = json.loads(comic)
            fileDict[fileName] = comic
    return fileDict


def insertToDataBase(fileDict):
    for fileName, value in fileDict.items():
        logger.info('--------------------------------------------')
        logger.info('处理文件 %s' % fileName)
        for comic in value:
            db.updateComic(comic)
        logger.info('移动文件 %s 至 %s' % (fileName, TODAY_FOLDER))
        os.rename(os.path.join(COLLECT_FOLDER,fileName), os.path.join(TODAY_FOLDER,fileName))
        logger.info('--------------------------------------------')


def main():
    if not os.path.isfile(db.DATABASE):
        logger.info('创建数据库 %s' % db.DATABASE)
        db.initDatabase()
    assert os.path.isdir(COLLECT_FOLDER), 'comic下不存在collect文件夹'
    if not os.path.isdir(TODAY_FOLDER):
        logger.info('创建文件夹 %s' % TODAY_FOLDER)
        os.mkdir(TODAY_FOLDER)
    fileList = list(filter(lambda x: x != 'done', os.listdir(COLLECT_FOLDER)))
    logger.info('将处理以下文件 %s' % str(fileList))
    fileDict = readJsonFile(fileList)
    logger.info('插入数据到数据库')
    insertToDataBase(fileDict)
    logger.info('结束')
    if len(os.listdir(TODAY_FOLDER)) == 0:
        logger.info('删除空文件夹 %s' % TODAY_FOLDER)
        os.rmdir(TODAY_FOLDER)


if __name__ == '__main__':
    main()