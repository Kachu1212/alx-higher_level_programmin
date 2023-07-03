#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    hop = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(hop.text.__class__))
    print("\t- content: {}".format(hop.text))
