import os
import json
import db
from db import logger

GENERATE_FOLDER = os.path.join('..', 'generate')

def generateIndex(comicIndex):
    indexStr = 'var index = \n' + json.dumps(comicIndex, ensure_ascii=False, indent=2)
    with open(os.path.join(GENERATE_FOLDER, 'index.js'), 'w', encoding='utf8') as indexFile:
        indexFile.write(indexStr)


def generateComic(comicIndex):
    for comic in comicIndex:
        comicPage = db.getComic(comic)
        comicStr = 'extLink[' + str(comic['编号']) + '] = \n' + json.dumps(comicPage, ensure_ascii=False, indent=2)
        with open(os.path.join(GENERATE_FOLDER, str(comic['编号']) + '.js'), 'w', encoding='utf8') as comicFile:
            logger.info('[%s] 创建%s文件' % (comic['名称'], str(comic['编号']) + '.js'))
            comicFile.write(comicStr)


def main():
    assert os.path.isfile(db.DATABASE), 'comic下数据库文件comic.db不存在，请双击collect.py来生成数据库并收集数据'
    if not os.path.isdir(GENERATE_FOLDER):
        logger.info('创建文件夹 %s' % GENERATE_FOLDER)
        os.mkdir(GENERATE_FOLDER)
    logger.info('从数据库中获取所有Comic数据')
    comicIndex = db.getIndex()
    logger.info('创建index.js文件')
    generateIndex(comicIndex)
    logger.info('创建generate下的文件')
    generateComic(comicIndex)


if __name__ == '__main__':
    main()