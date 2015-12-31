__author__ = 'Timur Mullayanov'
#__all__ = ["Joke", "Fetcher"]

# move all API methods and entities to package-level scope.
from icndb.Fetcher import fetchRandom
from icndb.Joke import Joke as Joke_

del Fetcher
del Joke

Joke = Joke_
del Joke_

print("Module initialized!")
