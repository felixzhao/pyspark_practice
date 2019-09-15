from unittest import TestCase
from run import func1

class TestFunc1(TestCase):
    def test_func1(self):
        self.assertEqual(func1(2), 4)
        #self.fail()
