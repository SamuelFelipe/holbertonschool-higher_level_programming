#!/usr/bin/python3

'''Use the urllib to fetch https://intranet.hbtn.io/status'''

import requests
from sys import argv

url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
req = requests.get(url, {'per_page': 10})

for i in req.json():
    print('{}: {}'.format(i['sha'], i['author']['login']))
