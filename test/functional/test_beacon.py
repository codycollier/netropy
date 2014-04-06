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
        self.assertTrue('outputValue' in rec)
        self.assertTrue(rec['statusCode'] in ('0', '1', '2'))

    def test_latest_timestamp(self):
        # This test could occasionally fail due to timing
        latest_timestamp = beacon.latest_timestamp()
        rec = beacon.current()
        self.assertEqual(latest_timestamp, rec['timeStamp'])

    def test_get_record(self):
        timestamp = beacon.latest_timestamp()
        rec = beacon.get_record(timestamp)
        self._basic_record_validation(rec)
        self.assertTrue(rec['statusCode'] == '0')

    def test_current(self):
        rec = beacon.current()
        self._basic_record_validation(rec)
        rec_last = beacon.last()
        self.assertEqual(rec, rec_last)
        self.assertTrue(rec['statusCode'] == '0')

    def test_previous(self):
        # get a couple records from 88 minutes back
        timestamp = beacon.latest_timestamp()
        timestamp = timestamp - (88 * 60)
        rec = beacon.get_record(timestamp)
        rec_prev = beacon.previous(timestamp)
        self._basic_record_validation(rec_prev)
        self.assertTrue(rec['previousOutputValue'] == rec_prev['outputValue'])

    def test_next(self):
        # get a couple records from 5 minutes back
        timestamp = beacon.latest_timestamp()
        timestamp = timestamp - (5 * 60)
        rec = beacon.get_record(timestamp)
        rec_next = beacon.next(timestamp)
        self._basic_record_validation(rec_next)
        self.assertTrue(rec['outputValue'] == rec_next['previousOutputValue'])

    def test_last(self):
        rec = beacon.last()
        self._basic_record_validation(rec)
        self.assertTrue(rec['statusCode'] == '0')

    def test_last_is_last(self):
        # This test could occasionally fail due to timing
        last_rec = beacon.last()
        self.assertRaises(Exception, beacon.next, last_rec['timeStamp'])

    def test_start_chain(self):
        timestamp = beacon.latest_timestamp()
        rec = beacon.start_chain(timestamp)
        self._basic_record_validation(rec)
        zero_val = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        self.assertTrue(rec['previousOutputValue'] == zero_val)
        self.assertTrue(rec['statusCode'] == '1')

    def test_start_is_first(self):
        timestamp = beacon.latest_timestamp()
        start_rec = beacon.start_chain(timestamp)
        self.assertRaises(Exception, beacon.previous, start_rec['timeStamp'])



if __name__ == "__main__":

    unittest.main()
