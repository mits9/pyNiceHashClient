import requests


# import json

def get_library_version():
    return 0.1


def get_api_version():
    response = requests.get("https://www.nicehash.com/api").json()
    return response['result']['api_version']
