import urllib.request
import urllib.parse
import json
import icndb.joke_extractor as Builder

__baseURL__ = 'http://api.icndb.com/'


def processNames(firstName=None, lastName=None):
    parameters = {}
    if firstName: parameters['firstName'] = firstName
    if lastName:  parameters['lastName']  = lastName
    return parameters


def limitCategories(queryParameters={}, limitTo=None, exclude=None):
    '''
    Internal function which appends query with limiting categories.
    If limitTo is non-empty list, parameter exclude will be ignored.
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

    Args:
        number (int, default=1): number of jokes to fetch.
            Must be positive integer.
        firstName, lastName (both str): names that are used to change
            the name of the main character when fetching a Joke.
        limitTo (None or list of str): list of categories
            which joke should be taken from.
        exclude (None or list of str): list of categories which joke
            should NOT be taken from.

    Returns:
        Instance of icndb.Joke class.
        If parameter number > 1, returns list of Jokes.

    Raises:
        TypeError: if number is not an integer
        ValueError: if number is non-positive.
    '''
    checkNumber(number) # raise an Exception if number is invalid
    url = "{}/jokes/random/{}".format(__baseURL__, number if number > 1 else '')
    queryParameters = limitCategories(processNames(firstName, lastName),
                             limitTo, exclude)
    if queryParameters:
        url = "{}?{}".format(url, urllib.parse.urlencode(queryParameters))

    return Builder.buildJokes(_requestJokes(url))


def _requestJokes(url):
    return json.loads( urllib.request.urlopen(url).read().decode('utf-8') )


def fetchByID(id, firstName=None, lastName=None):
    '''
    Fetches one joke with specified id
    Args:
        id (int): identifier of the joke in icndb.
        firstName, lastName (both str): names that are used to change
            the name of the main character when fetching a Joke.

    Returns:
        instance of a icndb.Joke class

    Raises:
        icndb.joke_extractor.JokeNotRetrieved: if id is bigger than result of
            fetchNumberOfJokes
        TypeError: if id is not an integer
        ValueError: if id is less than 0.
    '''
    checkNumber(id)
    if id > fetchNumberOfJokes():
        raise Builder.JokeNotRetrieved("Identifier is too big.")
    url = "{}/jokes/{}".format(__baseURL__, id)
    queryParameters = processNames(firstName, lastName)
    if queryParameters:
        url += "?{}".format(urllib.parse.urlencode(queryParameters))
    return Builder.buildJokes(_requestJokes(url))


def checkNumber(n):
    if not isinstance(n, int):
        raise TypeError("Given number is not integer!")
    elif n < 1:
        raise ValueError("Only positive integers are allowed!")


def fetchCategories():
    '''Returns list of available categories of jokes in icndb'''
    url = "{}/categories".format(__baseURL__)
    return _requestJokes(url)['value']


def fetchNumberOfJokes():
    '''Returns number of jokes in icndb'''
    url = "{}/jokes/count".format(__baseURL__)
    return _requestJokes(url)['value']
