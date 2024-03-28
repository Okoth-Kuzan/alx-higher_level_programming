#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
