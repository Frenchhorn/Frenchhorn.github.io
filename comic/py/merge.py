import os
import json
from db import db, DATABASE


# def validFileTime(fileList):
#     newFileList = []
#     for file in fileList:
#         if not fileDate or fileDate == os.path.getmtime('source/' + file):
#             continue
#         newFileList.append(file)
#     return newFileList


def readFile(fileList):
    fileDict = {}
    for i in fileList:
        with open(i, 'rb') as f:
            file = os.path.basename(i)
            comic = f.read()
            comic = comic.decode()
            comic = json.loads(comic)
            fileDict[file] = comic
    return fileDict


def insertDataBase(fileList):
    pass


def main():
    assert os.path.isfile(DATABASE), '双击db.py初始化数据库'
    db.connect()
    try:
        assert not ('source' in os.listdir('..')), '目录source不存在'
        fileList = os.listdir(os.path.join('..', 'source'))
        # fileList = validFileTime(fileList)
        fileDict = readFile(fileList)
        insertDataBase(fileList)
    finally:
        db.close()


if __name__ == '__main__':
    main()
