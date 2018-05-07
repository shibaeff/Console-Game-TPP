import unittest as ut
from src.abstract_classes import  abstract_classes as ac


class TestAbstract(ut.TestCase):
    def test_creation(self):
        abs_char  = ac.AbsCharacter("Jim", 2, 2, list())
        self.assertEquals(type(abs_char), ac.AbsCharacter)

        abs_manager = ac.AbsManager("Jim", 2, 2, 2, 2, list())
        self.assertEquals(type(abs_manager), ac.AbsManager)

        abs_tech = ac.AbsTech("Jim", 2, 2, 2, list())
        self.assertEquals(type(abs_tech), ac.AbsTech)


if __name__ == "__main__":
    ut.main()
