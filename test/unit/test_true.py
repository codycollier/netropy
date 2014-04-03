#!/usr/bin/env python


import unittest


class TestTrue(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_true(self):
        self.assertTrue(True)


if __name__ == "__main__":

    unittest.main()
