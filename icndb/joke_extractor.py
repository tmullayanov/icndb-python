'''
This module is responsible for getting Jokes from JSON.
In case data isn't correct ('type' != success), special exception is raised
'''

import json
from icndb.joke import Joke

class JokeNotRetrieved(ValueError): pass

def _check(JSON):
    if JSON['type'] != 'success':
        raise JokeNotRetrieved()


def buildJokes(jsonRsp):
    '''Parses content of recieved json to icndb.Joke (or list of them)'''
    _check(jsonRsp)
    value = jsonRsp['value']
    if isinstance(value, list):
        return [Joke(i['id'], i['joke']) for i in value]
    elif isinstance(value, dict):
        return Joke(value['id'], value['joke'])
