# TODO: add docs
# TODO: add config read
import logging
from camera_interface import CameraInterface
from controller import Camera


class WebotsCamera(CameraInterface):
    """[summary]

    Args:
        CameraInterface ([type]): [description]
    """

    def __init__(self, name, robot):
        super().__init__(name)
        self.robot = robot

        self.__wb_camera = Camera(self.name)
    
    def get_param(self, param_name):
        pass

    def start(self):
        try:
            self.__wb_camera.enable(100)
            self.__status = 'enabled'
        except Exception as start_exception:
            self.__status = 'disabled'
            logging.error(start_exception)

    def _get_image(self):
        image = None
        if self.__status == 'enabled':
            image = self.__wb_camera.getImage()
        else:
            logging.error("Camera is not started")
        return image

    def _get_height(self):
        height = None
        if self.__status == 'enabled':
            height = self.__wb_camera.getHeight()
        else:
            logging.error("Camera is not started")
        return height

    def _get_width(self):
        width = None
        if self.__status == 'enabled':
            width = self.__wb_camera.getWidth()
        else:
            logging.error("Camera is not started")
        return width
