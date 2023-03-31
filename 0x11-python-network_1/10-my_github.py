#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys


def get_github_id(username, password):
    """
    This function takes a username and password, and returns the user's
    GitHub ID
    """
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        return response.json().get("id")
    else:
        print("Error retrieving GitHub ID:", response.json().get("message"))
        sys.exit(1)


if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python3 github_id.py <username> <token>")
        sys.exit(1)

    # Get the username and password from the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Get the user's GitHub ID
    github_id = get_github_id(username, password)

    # Print the user's GitHub ID
    print(github_id)
