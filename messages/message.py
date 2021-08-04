from abc import ABCMeta
import logging


class Message:
    """[summary]

    Raises:
        Exception: [description]

    Returns:
        [type]: [description]
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.__timestamp = None

    @property
    def timestamp(self):
        """[summary]
        """
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        try:
            assert isinstance(timestamp, int, float)
            self.__timestamp = timestamp
        except AssertionError as assertion:
            logging.error("timestamp value must be an int or float")
            raise Exception("timestamp value must be an int or float") \
                from assertion
