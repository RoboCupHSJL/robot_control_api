# TODO: add docs
from abc import ABCMeta, abstractmethod
import logging
from communication import interactor

class ControllerInterface:
    """[summary]
    """
    __metaclass__ = ABCMeta
    def __init__(self, name, clock):
        self.__name__ = name
        self.hardware_interfaces = {}
        self._clock = clock

    @abstractmethod
    def step(self):
        """[summary]
        """

    def start(self):
        """[summary]
        """
        try:
            for hardware_interface in self.hardware_interfaces.values():
                hardware_interface.start()
                logging.info("Interface %s started successfully",
                             hardware_interface.name)
        except Exception as e:
            logging.error("Couldn't start interface %s. Exception is:\n%s",
                          hardware_interface.name, e)

    def stop(self):
        """[summary]
        """
        for hardware_interface in self.hardware_interfaces.values():
            hardware_interface.stop()

    def _add_interface(self, hardware_interface):
        """[summary]

        Args:
            hw (HardwareInterface): [description]
        """
        self.hardware_interfaces[hardware_interface.name] = hardware_interface
        logging.info("Added interface %s, type of %s ",
                     hardware_interface.name,
                     type(hardware_interface))
