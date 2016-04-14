import unittest
from math_functions import zero, fact
from unittest import TestCase


class SomeFunctionTests(TestCase):
    def test_zero(self):
        self.assertEquals(zero(5), 0)


class FactTest(TestCase):

    def setUp(self):
        print "setUP"

    def tearDown(self):
        print "tearDown"

    def test_fact0(self):
        self.assertEquals(fact(0), 1)

    def test_fact_positive(self):
        self.assertEquals(fact(5), 120)

    @unittest.expectedFailure
    def test_negative(self):
        y = fact(-1)

    @unittest.expectedFailure
    def test_correct_format(self):
        y = fact("abcd")


#if __name__ == "__main__":
#    unittest.main()