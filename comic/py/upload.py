import requests


def uploadImage(path):
    with open(path, 'rb') as f:
        req = requests.post('https://sm.ms/api/upload', params={'ssl':True, 'format':'json'}, files={'smfile':f})
        res = req.json()
    return res