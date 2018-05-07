from src.generation import generation as gen
import unittest as ut


class GenTest(ut.TestCase):
    def easy_test(self):
        managers_max = 10
        tech_max = 10
        for m in range(1, managers_max):
            for t in range(1, tech_max):
                pool = gen.Pool.gen_pool(t, m)
                self.assertIsNotNone(pool, "Pool was not correctly generated!")
                self.assertNotEqual(pool, list(), "Pool is emty!")


if __name__ == "__main__":
    ut.main()
