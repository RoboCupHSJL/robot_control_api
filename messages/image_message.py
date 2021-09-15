import logging
import numpy as np
from .message import Message


class ImageMessage(Message):
    """[summary]

    Args:
        Message ([type]): [description]
    """

    def __init__(self):
        super().__init__()
        self.__data = None
        self.__height = None
        self.__width = None
        self.__encoding = None

    @property
    def height(self) -> int:
        """[summary]
        """
        return self.__height

    @height.setter
    def height(self, height):
        try:
            assert isinstance(height, int)
            self.__height = height
        except AssertionError as assertion:
            logging.error("height value must be an int")
            raise Exception("height value must be an int") \
                from assertion

    @property
    def width(self) -> int:
        """[summary]
        """
        return self.__width

    @width.setter
    def width(self, width):
        try:
            assert isinstance(width, int)
            self.__width = width
        except AssertionError as assertion:
            logging.error("width value must be an int")
            raise Exception("width value must be an int") \
                from assertion

    @property
    def encoding(self) -> str:
        """[summary]
        """
        return self.__encoding

    @encoding.setter
    def encoding(self, encoding):
        try:
            assert isinstance(encoding, str)
            self.__encoding = encoding
        except AssertionError as assertion:
            logging.error("width value must be an str")
            raise Exception("width value must be an str") \
                from assertion

    @property
    def data(self) -> np.array:
        """[summary]
        """
        return self.__data

    @data.setter
    def data(self, *args):
        """[summary]

        Args:
            orientation ([type]): [description]
        """
        self.__data = np.array(args[0], dtype=float)
