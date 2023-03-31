#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter and displays
the body of the response.
"""

import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        content = response.read().decode('utf-8')

    print(content)
