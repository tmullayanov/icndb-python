__author__ = "Timur Mullayanov"

import urllib.request
import urllib.parse
import json
import icndb.JokeRetriever as Builder

__baseURL__ = 'http://api.icndb.com/'


def appendNames(url, firstName=None, lastName=None):
    d = {}
    if firstName: d['firstName'] = firstName
    if lastName:  d['lastName']  = lastName
    return "{}?{}".format(url, urllib.parse.urlencode(d))


def limitCategories(url, limitTo=None, exclude=None):
    '''
    Internal function which appends query with limiting categories.
    If limitTo is non-empty list, parameter @exclude will be ignored.

    @returns:
    '''
    if isinstance(limitTo, list):
        return "{}&{}".format(url, str(limitTo).translate(None, "'"))
    if isinstance(exclude, list):
        return "{}&{}".format(url, str(exclude).translate(None, "'"))
    return url


def fetchRandom(number=1, firstName=None, lastName=None,
    limitTo=None, exclude=None):
    '''
    Fetches arbitrary number of random jokes.

    @return: Instance of icndb.Joke.Joke class.
    If parameter number > 1, returns list of Jokes.
    '''
    checkNumber(number) # raise an Exception if number is invalid
    url = "{}/jokes/random".format(__baseURL__) # replace with call FormURL()
    url = limitCategories(appendNames(url, firstName, lastName),
                             limitTo, exclude)
    rawData = {}
    if (number > 1):
        return Builder.buildJokes(_requestJokes("{}/{}".format(url, number)))
    else:
        return Builder.buildJokes(_requestJokes(url))


def _requestJokes(url):
    return json.loads( urllib.request.urlopen(url).read().decode('utf-8') )


def fetchByID(id, firstName=None, lastName=None):
    checkNumber(id)
    url = "{}/jokes/{}".format(__baseURL__, id)
    url = appendNames(url, firstName, lastName)
    rawData = {}
    if (id > 1):
        return Builder.buildJokes(_requestJokes("{}/{}".format(url, id)))
    else:
        return Builder.buildJokes(_requestJokes(url))


def checkNumber(n):
    if not isinstance(n, int):
        raise TypeError("Given number is not integer!")
    elif n < 1:
        raise ValueError("Only positive integers are allowed!")


def fetchCategories():
    url = "{}/categories".format(__baseURL__)
    return _requestJokes(url)['value']
