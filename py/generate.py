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
        # if comic['卷'] + comic['话'] + comic['番外'] == 0:
        #     continue
        comicPage = db.getComic(comic)
        comicStr = 'extLink[' + str(comic['编号']) + '] = \n' + json.dumps(comicPage, ensure_ascii=False, indent=2)
        with open(os.path.join(GENERATE_FOLDER, str(comic['编号']) + '.js'), 'w', encoding='utf8') as comicFile:
            comicFile.write(comicStr)


def main():
    assert os.path.isfile(db.DATABASE), 'comic下数据库文件comic.db不存在，请双击collect.py来生成数据库'
    if not os.path.isdir(GENERATE_FOLDER):
        os.mkdir(GENERATE_FOLDER)
    comicIndex = db.getIndex()
    generateIndex(comicIndex)
    generateComic(comicIndex)


if __name__ == '__main__':
    main()