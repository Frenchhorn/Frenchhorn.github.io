import os
import json
from upload import uploadImages


def getPaths(folder):
    paths = []
    for folder_path, _, files in os.walk(folder):
        for file in files:
            paths.append(os.path.join(folder_path, file))
    return paths


if __name__ == '__main__':
    paths = getPaths(r'pics')
    print(paths)
    r = uploadImages(paths)
    if not r['errors']:
        with open('test.json', 'w') as f:
            f.write(json.dumps(r['results'], ensure_ascii=False, indent=2))
    else:
        print(r['errors'])