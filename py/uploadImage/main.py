import os
import json
import imghdr
from upload import uploadImages


def getPaths(folder):
    paths = []
    for folder_path, _, files in os.walk(folder):
        for file in files:
            path  = os.path.join(folder_path, file)
            if imghdr.what(path):
                paths.append(path)
    return paths


if __name__ == '__main__':
    paths = getPaths(r'pics')
    print(paths)
    r = uploadImages(paths)
    if not r['errors']:
        with open('pics.json', 'w') as f:
            f.write(json.dumps(r['results'], ensure_ascii=False, indent=2))
    else:
        print(r['errors'])