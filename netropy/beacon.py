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


import record


def _timestamp():
    pass


def _get_current_timestamp():
    pass


def _get_latest_timestamp():
    pass


def _retrieve_record():
    # record_xml = ...
    rec = record.parse_xml_record(record_xml)
    return rec


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


