__author__ = 'Timur Mullayanov'


class Joke(object):
    '''
    Class represents joke from ICNDB.
    All the fields are READ-ONLY.
    '''
    def __init__(self, id, text):
        self._id = id
        self._text = text

    def __setattr__(self, key, value):
        raise AttributeError("Set is not allowed!")

    @property
    def id(self):
        return self._id

    @property
    def text(self):
        return self._text

    def str(self):
        return "[Joke #{0}]{1}".format(self._id, self._text)

    def repr(self):
        return self.__str__()
