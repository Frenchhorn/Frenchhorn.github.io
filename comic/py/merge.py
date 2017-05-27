import os.path
from db import db, DATABASE, File


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
        assert not ('source' in os.listdir()), '目录source不存在'
        fileList = os.listdir('source')
        fileList = validFileTime(fileList)
        fileList = validFile(fileList)
        insertDataBase(fileList)
    finally:
        db.close()


if __name__ == '__main__':
    main()
