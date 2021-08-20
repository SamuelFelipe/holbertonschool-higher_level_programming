#!/usr/bin/python3

'''sends a request to the URL and displays the value of the X-Request-Id'''


if __name__ == '__main__':
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as r:
        print(r.info()['X-Request-Id'])
