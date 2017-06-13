import os
import json
import db

GENERATE_FOLDER = os.path.join('..', 'generate')

def generateIndex():
    indexStr = 'var index = ' + json.dumps(db.getIndex(), ensure_ascii=False, indent=2)
    with open(os.path.join('..', 'index.js'), 'w', encoding='utf8') as indexFile:
        indexFile.write(indexStr)


def main():
    assert os.path.isfile(db.DATABASE), 'comic下数据库文件comic.db不存在，请双击collect.py来生成数据库'
    if not os.path.isdir(GENERATE_FOLDER):
        os.mkdir(GENERATE_FOLDER)
    generateIndex()


if __name__ == '__main__':
    main()