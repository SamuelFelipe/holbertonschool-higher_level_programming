#!/usr/bin/python3

'''Use the urllib to fetch https://intranet.hbtn.io/status'''


if __name__ == '__main__':
    from sys import argv
    import requests

    url = argv[1]

    req = requests.get(url)

    print(req.headers['X-request-Id'])
