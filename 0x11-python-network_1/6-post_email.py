#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    payload = {"email": sys.argv[2]}
    hop = requests.post(sys.argv[1], data=payload)
    print(hop.text)
