"""record

"""


import collections


record_fields = ['version', 'frequency', 'timeStamp',
                 'seedValue', 'previousOutputValue',
                 'signatureValue', 'outputValue', 'statusCode']

Record = collections.namedtuple('Record', record_fields)


def verify_record(rec):
    """Verify a record by checking the signatureValue is valid

    From the schema file info for signatureValue:
    A digital signature (RSA) computed over (in order):
    version, frequency, timeStamp, randomValue, previousHashValue, errorCode
    Note: Except for version, the hash is on the byte representations
    and not the string representations of the data values

    """
    return True


def verify_pair(rec1, rec2):
    """Verify two records which are chained together"""
    return True


