#!/usr/bin/python3

'''github api'''


if __name__ == '__main__':
    import requests
    from sys import argv

    req = requests.Session()
    req.auth = (argv[1], argv[2])

    req = req.get('https://api.github.com/user')

    print(req.json()['id'])
