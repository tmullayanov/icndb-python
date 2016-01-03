__author__ = 'Timur Mullayanov'

# move all API methods and entities to package-level scope.
from icndb.fetcher import fetchRandom, fetchByID, \
fetchCategories, fetchNumberOfJokes
from icndb.joke import Joke

del fetcher
del joke_extractor
del joke

print("Module initialized!")
