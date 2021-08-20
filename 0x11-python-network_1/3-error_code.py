#!/usr/bin/python3

'''sends a request to the URL and displays the body of the response'''


if __name__ == '__main__':
    from sys import argv
    from urllib.request import urlopen
    from urllib.error import HTTPError

    try:
        with urlopen(argv[1]) as request:
            print(request.read().decode('utf-8'))
    except HTTPError as err:
        print('Error code: {}'.format(err.code))
