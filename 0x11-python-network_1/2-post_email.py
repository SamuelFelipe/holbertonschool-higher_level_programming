#!/usr/bin/python3

'''Use the urllib to fetch https://intranet.hbtn.io/status'''


if __name__ == '__main__':
    from sys import argv
    from urllib.request import urlopen
    from urllib.parse import urlencode

    data = {'email': argv[2]}
    data = urlencode(data)
    data = data.encode('ascii')

    with urlopen(argv[1], data) as f:
        print(f.read().decode('utf-8'))
