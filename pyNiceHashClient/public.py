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


def get_stats_provider(btc_address):
    request_uri = "https://www.nicehash.com/api?method=stats.provider"
    if btc_address != "":
        request_uri = request_uri + "&addr=" + str(btc_address)
    else:
        raise ValueError('Must provide valid bitcoin address')
    response = requests.get(request_uri).json()
    return response['result']


def get_buy_info():
    request_uri = "https://www.nicehash.com/api?method=buy.info"
    response = requests.get(request_uri).json()
    return response['result']
