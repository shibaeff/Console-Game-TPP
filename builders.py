import abstract_classes as ac
import manager_classes as mc
import tech_classes as tc
import abc

class AbsBuilder(metaclass=abc.ABCMeta):
    def __init__(self):
        self.__obj = ac.AbsCharacter(None, None, None, None)

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, val):
        self.__obj = val

    def set_to_obj(self, property, val):
        self.__obj.__dict__[property] = val

    def return_obj(self):
        ret = self.__obj
        self._purge()
        return ret

    def _purge(self):
        self.__obj = None

    def is_busy(self):
        return self.obj is not None


class AbsManagerBuilder(AbsBuilder):
    def __init__(self, char_class):
        self.obj = char_class(None, None, None, None, None, None, None)


class AbsTechBuilder(AbsBuilder):
    def __init__(self, char_class):
        self.obj = char_class(None, None, None, None, None, None)