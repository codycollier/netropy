"""beacon


rest api root:
    https://beacon.nist.gov/rest/

rest api example endpoints:
    https://beacon.nist.gov/rest/record/1395971640
    https://beacon.nist.gov/rest/record/previous/1395971640
    https://beacon.nist.gov/rest/record/next/1395971640
    https://beacon.nist.gov/rest/record/last/
    https://beacon.nist.gov/rest/record/start-chain/1395971640

"""


record_fields = ['version', 'frequency', 'timeStamp',
                 'seedValue', 'previousOutputValue',
                 'signatureValue', 'outputValue', 'statusCode']

Record = collections.namedtuple('Record', record_fields)


def _timestamp():
    pass


def _get_current_timestamp():
    pass


def _get_latest_timestamp():
    pass


def _validate_record():


def _parse_record():
    pass


def _retrieve_record():
    pass


def current():
    pass


def previous():
    pass


def next():
    pass


def last():
    pass


def start_chain():
    pass




