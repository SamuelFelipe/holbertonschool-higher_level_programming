#!/usr/bin/python3

'''Use the urllib to fetch https://intranet.hbtn.io/status'''


if __name__ == '__main__':
    from sys import argv
    from urllib.request import urlopen
    from urllib.parse import urlencode
    from urllib.error import HTTPError

    try:
        with urlopen(argv[1]) as request:
            print(request.read().decode('utf-8'))
    except HTTPError as err:
        print('Error code: {}'.format(err.code))
