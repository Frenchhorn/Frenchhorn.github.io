import os.path
import datetime
from db import db


def validFileTime(fileList):
    newFileList = []
    for file in fileList:
        fileDate = File.getFileDate(file)
        if not fileDate or fileDate == os.path.getmtime('source/' + file):
            continue
        newFileList.append(file)
    return newFileList


def validFile(fileList):
    return fileList


def insertDataBase(fileList):
    pass


def main():
    assert os.path.isfile(DATABASE), '双击db.py初始化数据库'
    db.connect()
    try:
        if 'source' in os.listdir() and os.path.isdir('source'):
            fileList = os.listdir('source')
        else:
            print("Can't find folder source")
            db.close()
            return False

        fileList = validFileTime(fileList)
        fileList = validFile(fileList)
        insertDataBase(fileList)
    finally:
        db.close()


if __name__ == '__main__':
    main()
