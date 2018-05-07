import unittest as ut
import src.item_classes.items as ac
from src.abstract_classes.abstract_classes import AbsCharacter


# class ItemTest(ut.TestCase):
#     def init_test(self):
#         some_item = ac.Item
#         some_char = AbsCharacter()
#         # wrapping up!
#         wrapped_char = some_item(some_char)
#
#         print(wrapped_char.__dict__)
#
#
# if __name__ == '__main__':
#     ut.main()

some_item = ac.Item
some_char = AbsCharacter('some', 1, 1, list())
# wrapping up!
wrapped_char = some_item(some_char)

print(wrapped_char)