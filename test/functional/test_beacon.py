#!/usr/bin/env python


import unittest

import beacon


class TestBeacon(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        # this is the standard frequency in the nist beacon right now
        self.frequency = 60

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def _basic_record_validation(self, rec):
        """Perform basic validation of a record dictionary"""
        #print(rec)
        self.assertTrue('timeStamp' in rec)

    def test_get_record(self):
        timestamp = beacon.latest_timestamp()
        rec = beacon.get_record(timestamp)
        self._basic_record_validation(rec)

    def test_current(self):
        rec = beacon.current()
        self._basic_record_validation(rec)

    def test_previous(self):
        timestamp = beacon.latest_timestamp()
        rec = beacon.previous(timestamp)
        self._basic_record_validation(rec)

    def test_next(self):
        timestamp = beacon.latest_timestamp()
        timestamp = timestamp - (5 * 60)
        rec = beacon.next(timestamp)
        self._basic_record_validation(rec)

    def test_last(self):
        rec = beacon.last()
        self._basic_record_validation(rec)

    def test_start_chain(self):
        timestamp = beacon.latest_timestamp()
        rec = beacon.start_chain(timestamp)
        self._basic_record_validation(rec)



if __name__ == "__main__":

    unittest.main()
