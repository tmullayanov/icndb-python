# icndb-python
Python API Wrapper for the Internet Chuck Norris Database http://www.icndb.com/api/

Requirements:
  Python 3.x
  
Usage:
```python
>>> import icndb
>>> joke = icndb.fetchRandom()
>>> print(joke)
>>> print(_ for _ in icndb.fetchRandom(number=5, firstName="Octo", lastName="Cat"))
```

More detailed example is located at ```tester.py```.

List of available functions:

  * ```fetchRandom(number, firstName, lastName, limitTo, exclude)```  - fetches ```number``` of random jokes from categories specified by ```limitTo``` or ```exclude``` with main character's name replaced with specified by ```firstName/lastName```.
  * ```fetchCategories``` - fetches list of available categories  
  * ```fetchNumberOfJokes``` - returns total amount of jokes in database 
  * ```fetchByID(id, firstName, lastName)``` - returns single joke from Database with main character's name replaced with specified by ```firstName/lastName```
