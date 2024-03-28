#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])
