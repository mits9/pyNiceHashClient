import requests

_BASE_URI = "https://www.nicehash.com/api"

def get_library_version():
    return '0.1.0'


def get_api_version():
    request_uri = _BASE_URI
    response = requests.get(request_uri).json()
    return response['result']['api_version']


def get_stats_global_current(location=None):
    request_uri = _BASE_URI + "?method=stats.global.current"
    if location is not None:
        request_uri = request_uri + "&location=" + str(location)
    response = requests.get(request_uri).json()
    return response['result']['stats']


def get_stats_global_24h(location=None):
    request_uri = _BASE_URI + "?method=stats.global.24h"
    if location is not None:
        request_uri = request_uri + "&location=" + str(location)
    response = requests.get(request_uri).json()
    return response['result']['stats']


def get_stats_provider(btc_address):
    request_uri = _BASE_URI + "?method=stats.provider"
    if btc_address != "":
        request_uri = request_uri + "&addr=" + str(btc_address)
    else:
        raise ValueError('Must provide valid bitcoin address')
    response = requests.get(request_uri).json()
    return response['result']


def get_buy_info():
    request_uri = _BASE_URI + "?method=buy.info"
    response = requests.get(request_uri).json()
    return response['result']


def get_orders(location, algo):
    request_uri = _BASE_URI + "?method=orders.get" \
                  + "&location=%s&algo=%s" % (location, algo)
    response = requests.get(request_uri).json()
    return response['result']
