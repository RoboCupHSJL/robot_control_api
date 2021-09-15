# TODO: add docs
from abc import abstractmethod
from hardware_interfaces.sensors import SensorInterface
from messages import ImageMessage


class CameraInterface(SensorInterface):
    """[summary]
    """
    def __init__(self, name, config, clock):
        super().__init__(name, clock)
        self.config = config

    @abstractmethod
    def _get_image(self):
        """[summary]
        """

    @abstractmethod
    def _get_height(self):
        """[summary]
        """

    @abstractmethod
    def _get_width(self):
        """[summary]
        """

    @abstractmethod
    def _get_encoding(self):
        """[summary]
        """

    def read(self):
        """[summary]

        Returns:
            [type]: [description]
        """

        msg = ImageMessage()
        image = self._get_image()

        if image is not None:

            msg.height = self._get_height()
            msg.width = self._get_width()
            # msg.is_bigendian = False
            # msg.step = self._get_width() * 4
            msg.data = image
            msg.encoding = self._get_encoding()

        return msg
