#!/usr/bin/env python

from nthprime import nthprime
import unittest

class KnownNthPrime(unittest.TestCase):

    def test1(self):
        self.assertEqual(11, nthprime(4))

    def test2(self):
        self.assertEqual(13, nthprime(5))

if __name__ == "__main__":
    unittest.main()
