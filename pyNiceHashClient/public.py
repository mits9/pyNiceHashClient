import requests
# import json

def get_library_version():
    return '0.1.0'


def get_api_version():
    request_uri = "https://www.nicehash.com/api"
    response = requests.get(request_uri).json()
    return response['result']['api_version']


def get_stats_global_current(location=None):
    request_uri = "https://www.nicehash.com/api?method=stats.global.current"
    if location is not None:
        request_uri = request_uri + "&location=" + str(location)
    response = requests.get(request_uri).json()
    return response['result']['stats']


def get_stats_global_24h(location=None):
    request_uri = "https://www.nicehash.com/api?method=stats.global.24h"
    if location is not None:
        request_uri = request_uri + "&location=" + str(location)
    response = requests.get(request_uri).json()
    return response['result']['stats']
