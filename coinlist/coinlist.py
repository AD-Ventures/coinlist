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
        res = requests.get(url)

        return CoinlistResponse(res.status_code == 200 and res.ok,
                             res.reason,
                             res.json())

    def getSymbol(self, symbol):
        url = '/symbols/' + symbol
        return self._publicRequest(url)

    def getSymbolCandles(self, symbol):
        url = '/symbols/' + symbol + '/candles'
        return self._publicRequest(url)

    def getSymbolAuctions(self, symbol):
        url = '/symbols/' + symbol + '/auctions'
        return self._publicRequest(url)

    def getSymbolOrders(self, symbol):
        url = '/symbols/' + symbol + '/book'
        return self._publicRequest(url)

    def getSymbolQuote(self, symbol):
        url = '/symbols/' + symbol + '/quote'
        return self._publicRequest(url)

    def getSymbolMarketSummary(self, symbol):
        url = '/symbols/' + symbol + '/summary'
        return self._publicRequest(url)

    def getAllSymbols(self):
        url = '/symbols/'
        return self._publicRequest(url)

    def getAllSymbolSummaries(self):
        url = '/symbols/summary'
        return self._publicRequest(url)

    def getSystemTime(self):
        url = '/time'
        return self._publicRequest(url)

    def getSupportedAssets(self):
        url = '/assets'
        return self._publicRequest(url)

    def getAuctionResult(self, symbol, auctionID):
        url = '/symbols/' + symbol + '/auctions/' + auctionID
        return self._publicRequest(url)
