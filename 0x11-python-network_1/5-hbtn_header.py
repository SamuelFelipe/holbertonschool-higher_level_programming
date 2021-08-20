#!/usr/bin/python3

'''sends a request to the URL'''


if __name__ == '__main__':
    from sys import argv
    import requests

    url = argv[1]
    req = requests.get(url)

    print(req.headers['X-request-Id'])
