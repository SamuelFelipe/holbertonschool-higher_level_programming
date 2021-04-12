#!/usr/bin/python3

'''Use the urllib to fetch https://intranet.hbtn.io/status'''


if __name__ == '__main__':
    import requests
    from sys import argv


    req = requests.get('https://api.github.com/repos/rails/rails/commits', {'per_page': 10})

    for i in req.json():
        print('{}: {}'.format(i['sha'], i['author']['login']))
