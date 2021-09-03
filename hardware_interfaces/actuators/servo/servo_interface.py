# TODO: add docs
from abc import abstractmethod
from hardware_interfaces.actuators import ActuatorInterface
from messages import ServoMessage


class ServoInterface(ActuatorInterface):
    """[summary]
    """
    def __init__(self, name, config, clock):
        super().__init__(name, clock)
        self.config = config

    @abstractmethod
    def _get_position(self):
        """[summary]
        """

    @abstractmethod
    def _set_position(self, goal_position):
        """[summary]
        """

    # TODO: add velocity and torque control
    # @abstractmethod
    # def _get_velocity(self):
    #     """[summary]
    #     """

    # @abstractmethod
    # def _set_velocity(self, goal_velocity):
    #     """[summary]
    #     """

    # @abstractmethod
    # def _get_torque(self):
    #     """[summary]
    #     """

    # @abstractmethod
    # def _set_torque(self, goal_torque):
    #     """[summary]
    #     """

    def read(self):
        """[summary]

        Returns:
            [type]: [description]
        """

        message = ServoMessage()
        message.position = self._get_position()
        return message

    def write(self, position):
        """[summary]

        Args:
            data ([type]): [description]
        """
        self._set_position(position)
