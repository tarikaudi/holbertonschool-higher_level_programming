#!/usr/bin/python3
"""comment for the""" 

import urllib.request

if __name__ == "__main__":

    url = "https://intranet.hbtn.io/status"
    data_req = urllib.request.Request(url)

    with urllib.request.urlopen(data_req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode("utf8"))
