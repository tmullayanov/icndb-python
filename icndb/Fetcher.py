__author__ = "Timur Mullayanov"

import urllib.request
import urllib.parse
import json
import icndb.JokeRetriever as Builder

__baseURL__ = 'http://api.icndb.com/'


def appendNames(url, firstName=None, lastName=None):
    parameters = {}
    if firstName: parameters['firstName'] = firstName
    if lastName:  parameters['lastName']  = lastName
    return parameters


def limitCategories(queryParameters, limitTo=None, exclude=None):
    '''
    Internal function which appends query with limiting categories.
    If limitTo is non-empty list, parameter @exclude will be ignored.
    '''

    tbl = str.maketrans('', '', "'\"")
    if isinstance(limitTo, list):
        queryParameters['limitTo'] = str(limitTo).translate(tbl)
    elif isinstance(exclude, list):
        queryParameters['exclude'] = str(limitTo).translate(tbl)
    return queryParameters


def fetchRandom(number=1, firstName=None, lastName=None,
    limitTo=None, exclude=None):
    '''
    Fetches arbitrary number of random jokes.

    @return: Instance of icndb.Joke.Joke class.
    If parameter number > 1, returns list of Jokes.
    '''
    checkNumber(number) # raise an Exception if number is invalid
    url = "{}/jokes/random/{}".format(__baseURL__, number if number > 1 else '')
    queryParameters = limitCategories(appendNames(url, firstName, lastName),
                             limitTo, exclude)
    if queryParameters:
        url = "{}?{}".format(url, urllib.parse.urlencode(queryParameters))

    return Builder.buildJokes(_requestJokes(url))


def _requestJokes(url):
    return json.loads( urllib.request.urlopen(url).read().decode('utf-8') )


def fetchByID(id, firstName=None, lastName=None):
    checkNumber(id)
    url = "{}/jokes/{}".format(__baseURL__, id)
    queryParameters = appendNames(url, firstName, lastName)
    if queryParameters:
        url += "?{}".format(urllib.parse.urlencode(queryParameters))
    return Builder.buildJokes(_requestJokes(url))


def checkNumber(n):
    if not isinstance(n, int):
        raise TypeError("Given number is not integer!")
    elif n < 1:
        raise ValueError("Only positive integers are allowed!")


def fetchCategories():
    url = "{}/categories".format(__baseURL__)
    return _requestJokes(url)['value']
