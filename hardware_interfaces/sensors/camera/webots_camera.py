# TODO: add docs
# TODO: add config read
import logging
from .camera_interface import CameraInterface
from controller import Camera


class WebotsCamera(CameraInterface):
    """[summary]

    Args:
        CameraInterface ([type]): [description]
    """

    def __init__(self, name, agent, config, clock):
        super().__init__(name, config, clock)
        self.agent = agent

        self.__wb_camera = Camera(self.name)

    def get_param(self, param_name):
        result = None
        if param_name == "height":
            result = self._get_height()
        elif param_name == "width":
            result = self._get_width()
        elif param_name == "encoding":
            result = self._get_encoding()
        return result

    def start(self):
        try:
            self.__wb_camera.enable(100)
            self.status = 'enabled'
        except Exception as start_exception:
            self.status = 'disabled'
            logging.error(start_exception)

    def _get_image(self):
        image = None
        if self.status == 'enabled':
            image = self.__wb_camera.getImageArray()
        else:
            logging.error("Camera is not started")
        return image

    def _get_height(self):
        height = None
        if self.status == 'enabled':
            height = self.__wb_camera.getHeight()
        else:
            logging.error("Camera is not started")
        return height

    def _get_width(self):
        width = None
        if self.status == 'enabled':
            width = self.__wb_camera.getWidth()
        else:
            logging.error("Camera is not started")
        return width

    def _get_encoding(self):
        return "bgra8"
