#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status and
using request package displays the body of the response.
"""

import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
