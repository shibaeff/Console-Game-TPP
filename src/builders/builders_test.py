import unittest as ut
from src.builders import builders as bd
from src.tech_classes import tech_classes as tc
from src.manager_classes import manager_classes as mc


class TestBuilders(ut.TestCase):
    def test_tech_builder_inst(self):
        for class_name in tc.tech_classes_list:
            builder = bd.AbsTechBuilder(class_name)
            product = builder.return_obj()
            self.assertEquals(type(product), class_name)

    def test_man_builder(self):
        for class_name in mc.manager_classes_list:
            builder = bd.AbsManagerBuilder(class_name)
            product = builder.return_obj()
            self.assertEquals(type(product), class_name)

if __name__ == "__main__":
    ut.main()
