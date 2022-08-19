#!/usr/bin/python3
"""comment for the checker"""

import requests
from sys import argv

if __name__ == "__main__":
    params = {'email': argv[2]}
    request = requests.post(argv[1], data=params)
    print(request.text)
