# TODO: add docs
from abc import ABCMeta, abstractmethod


class HardwareInterface:
    """[summary]
    """
    __metaclass__ = ABCMeta

    def __init__(self, name):

        """[summary]
        """
        self.__name = name
        self.__interface_type = type(self)
        self.__status = 'disabled'

    @abstractmethod
    def get_param(self, param_name):
        """[summary]
        """

    @abstractmethod
    def start(self):
        """[summary]
        """

    @abstractmethod
    def stop(self):
        """[summary]
        """

    @property
    def name(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__name

    @property
    def status(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__status

    @status.setter
    def status(self, status):
        """[summary]

        Returns:
            [type]: [description]
        """
        self.__status = status

    @property
    def interface_type(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__interface_type
