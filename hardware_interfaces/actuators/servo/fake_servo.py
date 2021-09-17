# TODO: add docs
import logging
from .servo_interface import ServoInterface
from controller import PositionSensor, Motor


class FakeServo(ServoInterface):
    """[summary]

    Args:
        ServoInterface ([type]): [description]
    """
    def __init__(self, name, agent, config, clock):
        super().__init__(name, config, clock)
        self.current_position = 0

    def start(self):
        self.status = 'enabled'

    def _get_position(self):
        """[summary]

        Returns:
            [type]: [description]
        """

        return self.current_position

    def _set_position(self, goal_position):
        """[summary]

        Args:
            ang ([type]): [description]
        """
        self.current_position = goal_position
