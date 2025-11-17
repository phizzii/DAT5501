import unittest
from Week1 import littleFunction

class testlittleFunction(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(littleFunction(2,3),5)
        self.assertEqual(littleFunction(-1,-4),-5)
        self.assertEqual(littleFunction(0,0), 0)
        