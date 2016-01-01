__author__ = 'Timur Mullayanov'


class Joke(object):
    '''
    Class represents joke from ICNDB.
    All the fields are READ-ONLY.
    '''
    __slots__ = ("_id", "_text")

    def __init__(self, id, text):
        super(Joke, self).__setattr__("_id", id)
        super(Joke, self).__setattr__("_text", text)

    def __setattr__(self, key, value):
        raise AttributeError("Set is not allowed!")

    @property
    def id(self):
        return self._id

    @property
    def text(self):
        return self._text

    def __str__(self):
        return "\"[Joke #{0}] {1}\"".format(self._id, self._text)

    def __repr__(self):
        return self.__str__()
