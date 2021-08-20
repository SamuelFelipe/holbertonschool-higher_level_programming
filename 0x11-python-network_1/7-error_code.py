#!/usr/bin/python3

'''sends a request to the URL and displays the body of the response'''


if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get(argv[1])

    if not (r.status_code == requests.codes.ok):
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
