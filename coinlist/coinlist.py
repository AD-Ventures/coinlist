import hashlib
import hmac
import json


import requests


from time import time


class CoinlistResponse:
    """A class to handle responses from calls to the Coinlist API"""



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
        res = requests.get(url)

        return TxbitResponse(res.ok and res.json()['success'],
                             res.json()['message'],
                             res.json()['result'])
