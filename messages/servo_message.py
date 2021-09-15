# TODO: add docs
import logging
from .message import Message


class ServoMessage(Message):
    """[summary]

    Raises:
        Exception: [description]

    Returns:
        [type]: [description]
    """

    def __init__(self):
        super().__init__()
        self.__position = None
        self.__velocity = None
        self.__torque = None

    @property
    def position(self):
        """[summary]
        """
        return self.__position

    @position.setter
    def position(self, *args):
        """[summary]

        Args:
            position (float):servo position in radians
        """
        if isinstance(args[0], float) and len(args) == 1:
            self.__position = args[0]
        else:
            logging.error("Invalid position type. Expected float, got %s", type(args[0]))

    @property
    def velocity(self):
        """[summary]
        """
        return self.__velocity

    @velocity.setter
    def velocity(self, *args):
        """[summary]

        Args:
            position (float):servo velocity in radians
        """
        if isinstance(args[0], float) and len(args) == 1:
            self.__velocity = args[0]
        else:
            logging.error("Invalid velocity type. Expected float, got %s", type(args[0]))

    @property
    def torque(self):
        """[summary]
        """
        return self.__torque

    @torque.setter
    def torque(self, *args):
        """[summary]

        Args:
            torque (float):servo torque in radians
        """
        if isinstance(args[0], float) and len(args) == 1:
            self.__torque = args[0]
        else:
            logging.error("Invalid torque type. Expected float, got %s", type(args[0]))
