import os, sys, json, imghdr
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
    paths = getPaths(sys.argv[1])
    print(paths)
    r = uploadImages(paths)
    file_name = os.path.basename(sys.argv[1]) + '.json'
    with open(file_name, 'w') as f:
        f.write(json.dumps(r['results'], ensure_ascii=False, indent=2))
    if r['errors']:
        with open('errors.json', 'w') as f:
            f.write(json.dumps(r['errors'], ensure_ascii=False, indent=2))