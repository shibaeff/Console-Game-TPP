import unittest as ut
from src.tech_classes import tech_classes as tc


class TestTechClasses(ut.TestCase):
    def test_creation(self):
        for class_name in tc.tech_classes_list:
            new_obj = class_name("Jim", 2, 2, 2, 2, list())
            self.assertEquals(type(new_obj), class_name)


if __name__ == "__main__":
    ut.main()

