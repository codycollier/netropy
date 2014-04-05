"""record

"""


import collections
import hashlib


record_fields = ['version', 'frequency', 'timeStamp',
                 'seedValue', 'previousOutputValue',
                 'signatureValue', 'outputValue', 'statusCode']

Record = collections.namedtuple('Record', record_fields)


def verify_record(record):
    """Verify a record is internally consistent

    signatureValue - This can't be verified as there is no public key
    outputValue - This should be a hash of the signatureValue

    From the schema file info for outputValue:
    The SHA-512 hash of the signatureValue as a 64 byte hex string

    ALERT! - broken
    This isn't working as expected. The outputValue is not matching a sha-512
    hash of the signatureValue.
    """
    signature_value = record['signatureValue']
    output_value = record['outputValue']
    sv_hash = hashlib.sha512(signature_value).hexdigest()
    return sv_hash == output_value


def verify_pair(record1, record2):
    """Verify two records which are chained together

    Any given record (except the first) should be chained to the previous
    by a matching hash in previousOutputValue.

    From the schema file info for outputValue:
    The SHA-512 hash value for the previous record - 64 byte hex string
    
    """
    rec1_output_value = record1['outputValue']
    rec2_previous_output_value = record2['previousOutputValue']
    return rec1_output_value == rec2_previous_output_value


