__author__ = "Timur Mullayanov"

import urllib.request
import json
import icndb.JokeRetriever as Builder

__baseURL__ = 'http://api.icndb.com/'

#TODO: add feature with names replacement
#NOTE: final name just should be passed as argument to all FETCH functions
# and correctly be passed to web-DB

def fetchRandom(number=1):
    checkNumber(number) # raise an Exception if number is invalid
    url = "{}/jokes/random".format(__baseURL__) # replace with call FormURL()
    rawData = {}
    if (number > 1):
        return Builder.buildJokes(_requestJokes("{}/{}".format(url, number)))
    else:
        return Builder.buildJokes(_requestJokes(url))


def _requestJokes(url):
    return urllib.request.urlopen(url).read().decode('utf-8')


def fetchByID():
    pass


def checkNumber(n):
    if not isinstance(n, int):
        raise TypeError("Given number of jokes is not integer!")
    elif n < 1:
        raise ValueError("Only positive integers are allowed!")
