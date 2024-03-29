#!/usr/bin/python3
"""comment for the checker"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email})

    data = data.encode()
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode())
