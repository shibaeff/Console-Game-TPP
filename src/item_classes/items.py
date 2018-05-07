"""
Every items wraps around the character object adding new behaviour.
"""
from src.abstract_classes.abstract_classes import AbsCharacter


class Item(object):
    def __init__(self):
        """
        Maybe this init might come in handy some day
        """
        pass

    def wrap(self, char: AbsCharacter):
        self._char = char
        # it's good to know how character was decorated
        self._char.possessions.append(self)

    def __getattr__(self, item):
        """
        Provide access to wrapped object's methods
        :param item:
        :return:
        """
        return getattr(self._man, item)

