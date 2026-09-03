class BhavcopyNotAvailableError(Exception):
    """this error could occur in case you download bhavcopy for the dates
    when the market was close"""


class DateFormatError(Exception):
    """in case the date format is errorneous"""
