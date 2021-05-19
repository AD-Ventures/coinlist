import hashlib
import hmac
import json


import requests


from time import time


class CoinlistResponse:
    """A class to handle responses from calls to the Coinlist API"""
    def __init__(self, success, message, result):
        self.success = success
        self.message = message
        self.result = result

    def __str__(self):
        d = {
            'success': self.success,
            'message': self.message,
            'result': self.result
        }
        return str(json.dumps(d, indent = 4))

class Coinlist:
    """A class to interact with the Coinlist API
    Attributes"""
    endpoint = 'https://trade-api.coinlist.co/v1'

    def __init__(self, APIKey=None, Secret=None):
        self.APIKey = APIKey
        self.Secret = Secret

    def _expandPathToUrl(self, path, params={}):
        """adds onto the base url for specific methods"""
        url = self.endpoint + path
        url += '?' if params else ''
        return url + '&'.join([key + '=' + str(params[key]) for key in params])

    def _publicRequest(self, path, params={}):
        """public call for Public Methods"""
        url = self._expandPathToUrl(path, params)
        print(url)
        res = requests.get(url)

        return CoinlistResponse(res.status_code == 200,
                             res.reason,
                             res.json())

    def getSymbols(self, symbol):
        url = '/symbols/' + symbol
        return self._publicRequest(url)

coin = Coinlist();

ret = coin.getSymbols('BTC-USD')

print(ret)
