# TODO: add docs
from abc import abstractmethod
from sensor_interface import SensorInterface
from messages import IMUMessage


class IMUSensorInterface(SensorInterface):
    """[summary]
    """

    @abstractmethod
    def _get_orientation(self):
        """[summary]
        """

    # TODO: implement linear_acceleration and angular_velocity
    # @abstractmethod
    # def _get_linear_accleration(self):
    #     """[summary]
    #     """

    # @abstractmethod
    # def _get_angular_velocity(self):
    #     """[summary]
    #     """

    def read(self):
        """[summary]

        Returns:
            [type]: [description]
        """

        msg = IMUMessage()
        msg.orientation = self._get_orientation()
        return msg
