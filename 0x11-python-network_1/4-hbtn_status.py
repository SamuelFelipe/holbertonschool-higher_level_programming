#!/usr/bin/python3

'''fetches https://intranet.hbtn.io/status'''


if __name__ == '__main__':
    import requests

    req = requests.get('https://intranet.hbtn.io/status')
    print('''Body response:
\t- type: {}
\t- content: {}'''.format(type(req.text), req.text))
