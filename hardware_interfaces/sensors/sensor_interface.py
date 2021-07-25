# TODO: add docs
from abc import abstractmethod
from hardware_interfaces import HardwareInterface


class SensorInterface:
    """[summary]
    """
    __metaclass__ = HardwareInterface

    @abstractmethod
    def read(self):
        """[summary]
        """
