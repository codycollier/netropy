#!/usr/bin/env python


import unittest

import record


class TestRecord(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.start_rec = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <record>
            <version>Version 1.0</version>
            <frequency>60</frequency>
            <timeStamp>1378395540</timeStamp>
            <seedValue>87F49DB997D2EED0B4FDD93BAA4CDFCA49095AF98E54B81F2C39B5C4002EC04B8C9E31FA537E64AC35FA2F038AA80730B054CFCF371AB5584CFB4EFD293280EE</seedValue>
            <previousOutputValue>00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</previousOutputValue>
            <signatureValue>F93BBE5714944F31983AE8187D5D94F87FFEC2F98185F9EB4FE5DB61A9E5119FB0756E9AF4B7112DEBF541E9E53D05346B7358C12FA43A8E0D695BFFAF193B1C3FFC4AE7BCF6651812B6D60190DB8FF23C9364374737F45F1A89F22E1E492B0F373E4DB523274E9D31C86987C64A26F507008828A358B0E166A197D433597480895E9298C60D079673879C3C1AEDA6306C3201991D0A6778B21462BDEBB8D3776CD3D0FA0325AFE99B2D88A7C357E62170320EFB51F9749B5C7B9E7347178AB051BDD097B226664A2D64AF1557BB31540601849F0BE3AAF31D7A25E2B358EEF5A346937ADE34A110722DA8C037F973350B3846DCAB16C9AA125F2027C246FDB3</signatureValue>
            <outputValue>17070B49DBF3BA12BEA427CB6651ECF7860FDC3792268031B77711D63A8610F4CDA551B7FB331103889A62E2CB23C0F85362BBA49B9E0086D1DA0830E4389AB1</outputValue>
            <statusCode>1</statusCode>
        </record>
        """

        self.rec1 = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <record>
            <version>Version 1.0</version>
            <frequency>60</frequency>
            <timeStamp>1396659060</timeStamp>
            <seedValue>162F65BA5BF336D69BEF6F39E170EC34BB68E3207A56463D21DC4C5DD45936FF9D2498F08E25B39200D623D034EE6C941B80FCDB3B875D497348A6ECEFB6232F</seedValue>
            <previousOutputValue>73455B6BC0D0A837D04ECFB0E677136440C173F77FC3C6995348078D194F0061710287A213771333E6C846802736A396E75D60BD86A261130B3B60E402347E80</previousOutputValue>
            <signatureValue>42D2E9F0F3F761DB08FB50445940AB4ACD24B42516FB88DC8D0679AF0D50A2652A38CD7789F3B5708755EC7F4FF64AC8F6928ABDFFC4F46337BC415B1A1286F4B928EA7D8A6537DE4248B707207A65D52714AA588BECBA0AC16FDAFBB9965F31DBC87E7E7EB814BDC597C64BA7EF5143969F4956BA43059CE85E7ECEF892936AA237E4DE793B85FB7D9CBD658F796ACC22E981285BCD235C618D38E806DF65D0477359831B4BB11A29BAACA219316FAFCA12DFB5D12C436E407E4A78AB55E63233F9AA688EFE75B15F9421ACCEEAD963B9D448730404D4B0F72ABF2CEAD7615414007C15C409049451889C177CB34674AC04E1BCC52FF74BA0E82B6303E7845F</signatureValue>
            <outputValue>736735E3A5A7CDDB2CE3DE9C43BB5BAFA93A5D2DCC58C1868CBB903FBD319D760709988F3DE340883EDA2B4F982CE7B2C8F2DB540791A83A19EAFE01EFF3544E</outputValue>
            <statusCode>0</statusCode>
        </record>
        """

        self.rec2 = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <record>
            <version>Version 1.0</version>
            <frequency>60</frequency>
            <timeStamp>1396659060</timeStamp>
            <seedValue>162F65BA5BF336D69BEF6F39E170EC34BB68E3207A56463D21DC4C5DD45936FF9D2498F08E25B39200D623D034EE6C941B80FCDB3B875D497348A6ECEFB6232F</seedValue>
            <previousOutputValue>73455B6BC0D0A837D04ECFB0E677136440C173F77FC3C6995348078D194F0061710287A213771333E6C846802736A396E75D60BD86A261130B3B60E402347E80</previousOutputValue>
            <signatureValue>42D2E9F0F3F761DB08FB50445940AB4ACD24B42516FB88DC8D0679AF0D50A2652A38CD7789F3B5708755EC7F4FF64AC8F6928ABDFFC4F46337BC415B1A1286F4B928EA7D8A6537DE4248B707207A65D52714AA588BECBA0AC16FDAFBB9965F31DBC87E7E7EB814BDC597C64BA7EF5143969F4956BA43059CE85E7ECEF892936AA237E4DE793B85FB7D9CBD658F796ACC22E981285BCD235C618D38E806DF65D0477359831B4BB11A29BAACA219316FAFCA12DFB5D12C436E407E4A78AB55E63233F9AA688EFE75B15F9421ACCEEAD963B9D448730404D4B0F72ABF2CEAD7615414007C15C409049451889C177CB34674AC04E1BCC52FF74BA0E82B6303E7845F</signatureValue>
            <outputValue>736735E3A5A7CDDB2CE3DE9C43BB5BAFA93A5D2DCC58C1868CBB903FBD319D760709988F3DE340883EDA2B4F982CE7B2C8F2DB540791A83A19EAFE01EFF3544E</outputValue>
            <statusCode>0</statusCode>
        </record>
        """

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_true(self):
        self.assertTrue(True)

    def test_verify_record(self):
        pass


if __name__ == "__main__":

    unittest.main()
