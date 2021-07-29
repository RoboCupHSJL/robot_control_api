import logging

class ImageMessage:
    

    def __init__(self):
        self.__timestamp = None
        self.__data = None
        self.__height = None
        self.__width = None

    @property
    def timestamp(self):
        """[summary]
        """
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        try:
            assert isinstance(timestamp, (int, float))
            self.__timestamp = timestamp
        except AssertionError as assertion:
            logging.error("timestamp value must be an int or float")
            raise Exception("timestamp value must be an int or float") \
                from assertion

    @property
    def height(self):
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
    def width(self):
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
    def data(self):
        """[summary]
        """
        return self.__data

    @data.setter
    def data(self, *args):
        """[summary]

        Args:
            orientation ([type]): [description]
        """
        assert isinstance(args[0], (tuple, list)) and \
            len(args[0]) == self.__height and len(args[0][0]) == self.__width
        self.__data = args[0]
