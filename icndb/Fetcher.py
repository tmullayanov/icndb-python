__author__ = "Timur Mullayanov"

import urllib.request
import json

#TODO: implement class derived from any Exception for negative joke number
#class

__baseURL__ = 'http://api.icndb.com/'


def fetchRandom(number=1):
    checkNumber(number) # raise an Exception if number is invalid
    url = "{}/jokes/random".format(__baseURL__)
    rawData = {}
    if (number > 1):
        return _requestJokes("{}/{}".format(url, number))
    else:
        return _requestJokes(url)

def _requestJokes(url):
    return urllib.request.urlopen(url).read().decode('utf-8')


def fetchByID():
    pass


def checkNumber(n):
    if not isinstance(n, int):
        raise TypeError("Given number of jokes is not integer!")
    elif n < 1:
        raise ValueError("Only positive integers are allowed!")
