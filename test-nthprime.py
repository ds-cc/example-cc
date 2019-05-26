#!/usr/bin/env python

from nthprime import nthprime
from unittest import TestCase

class KnownNthPrime(TestCase):

    def test1(self):
        self.assertEqual(11, nthprime(5))

    def test2(self):
        self.assertEqual(13, nthprime(6))
