import os
from upload import uploadImages
from pprint import pprint


def getPaths(folder):
    paths = []
    for folder_path, _, files in os.walk(folder):
        for file in files:
            paths.append(os.path.join(folder_path, file))
    return paths


if __name__ == '__main__':
    paths = getPaths(r'C:\Users\qinpan.zhao\Desktop\Share\image2url\pics')
    pprint(paths)
    r = uploadImages(paths)