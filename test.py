#! /usr/bin/env python

import unittest
from sha2 import *

class TestSHA512(unittest.TestCase):
    def setUp(self):
        self.f = sha512

    def test_empty(self):
        self.assertEqual(self.f('').hexdigest(),
                         'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce'+
                         '47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e')

    def test_less_than_block_length(self):
        self.assertEqual(self.f('abc').hexdigest(),
                         'ddaf35a193617abacc417349ae20413112e6fa4e89a97ea20a9eeee64b55d39a'+
                         '2192992a274fc1a836ba3c23a3feebbd454d4423643ce80e2a9ac94fa54ca49f')

    def test_block_length(self):
        self.assertEqual(self.f('a'*128).hexdigest(),
                         'b73d1929aa615934e61a871596b3f3b33359f42b8175602e89f7e06e5f658a24'+
                         '3667807ed300314b95cacdd579f3e33abdfbe351909519a846d465c59582f321')

    def test_several_blocks(self):
        self.assertEqual(self.f('a'*1000000).hexdigest(),
                         'e718483d0ce769644e2e42c7bc15b4638e1f98b13b2044285632a803afa973eb'+
                         'de0ff244877ea60a4cb0432ce577c31beb009c5c2c49aa2e4eadb217ad8cc09b')

if __name__ == '__main__':
    sha512_suite = unittest.TestLoader().loadTestsFromTestCase(TestSHA512)

    all_tests = unittest.TestSuite([sha512_suite])

    unittest.TextTestRunner(verbosity=2).run(all_tests)
