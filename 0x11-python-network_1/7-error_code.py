#!/usr/bin/python3

'''Use the urllib to fetch https://intranet.hbtn.io/status'''


if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get(argv[1])

    if not (r.status_code == requests.codes.ok):
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
