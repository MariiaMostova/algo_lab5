import unittest
from electr import *


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_the_worst('heights1.txt'), 5.66)

    def test2(self):
        self.assertEqual(get_the_worst('heights2.txt'), 300)

    def test3(self):
        self.assertEqual(get_the_worst('heights3.txt'), 392.32)

    def test4(self):
        self.assertEqual(get_the_worst('heights4.txt'), 2755.96)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(MyTestCase())
