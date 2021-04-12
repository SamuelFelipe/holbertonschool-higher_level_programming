#!/usr/bin/python3

'''Use the urllib to fetch https://intranet.hbtn.io/status'''


if __name__ == '__main__':
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as request:
        print(request.info()['X-Request-Id'])
