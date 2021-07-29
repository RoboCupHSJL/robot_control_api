# TODO: add docs
from abc import abstractmethod
from sensor_interface import SensorInterface
from messages import ImageMessage

class CameraInterface(SensorInterface):
    """[summary]
    """

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

    def read(self):
        """[summary]

        Returns:
            [type]: [description]
        """

        msg = ImageMessage()
        image = self._get_image()

        if image is None:
            return

        msg.height = self._get_height()
        msg.width = self._get_width()
        #msg.is_bigendian = False
        #msg.step = self._get_width() * 4
        msg.image = image
        #msg.encoding = 'bgra8'

        return msg