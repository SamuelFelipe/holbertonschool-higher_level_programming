#!/usr/bin/python3

'''Use the urllib to fetch https://intranet.hbtn.io/status'''


if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) < 2:
        q = {'q': ''}
    else:
        q = {'q': argv[1]}

    req = requests.post(url, q)

    data = req.json()

    try:
        if data:
            print('[{}] {}'.format(data['id'], data['name']))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
