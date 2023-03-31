#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the header
of the response.
"""
import urllib.request
import sys


def print_header(url):
    """Prints the value of the X-Request-Id header in the response."""
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    print_header(url)
