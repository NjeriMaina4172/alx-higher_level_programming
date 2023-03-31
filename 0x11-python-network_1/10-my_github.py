#!/usr/bin/python3

"""
This script takes your GitHub credentials (username and password) and uses the
GitHub API to display your id.

Usage: ./github_id.py <username> <password>
"""

import requests
import sys

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage: ./github_id.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    url = f'https://api.github.com/users/{username}'

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:

        user_id = response.json().get('id')

        if user_id is not None:
            print(user_id)
        else:
            print('No user ID found in response.')
            sys.exit(1)
    else:
        print(f'Request failed with status code {response.status_code}.')
        sys.exit(1)
