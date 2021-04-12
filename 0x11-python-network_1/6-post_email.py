#!/usr/bin/python3

'''Use the urllib to fetch https://intranet.hbtn.io/status'''


if __name__ == '__main__':
    import requests
    from sys import argv

    req = requests.post(argv[1], {'email': argv[2]})

    print(req.text)
