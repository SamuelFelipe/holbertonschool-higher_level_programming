#!/usr/bin/python3

'''fetches https://intranet.hbtn.io/status'''


if __name__ == '__main__':
    from urllib.request import urlopen

    with urlopen('https://intranet.hbtn.io/status') as r:
        body = r.read()
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- utf8 content: {}'.format(body.decode('utf-8')))
