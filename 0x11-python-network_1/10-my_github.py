#!/usr/bin/python3

'''Use the urllib to fetch https://intranet.hbtn.io/status'''


if __name__ == '__main__':
    import requests
    from sys import argv

    s = requests.Session()
    s.auth = (argv[1], argv[2])

    req = s.get('https://api.github.com/user')

    print(req.json()['id'])
