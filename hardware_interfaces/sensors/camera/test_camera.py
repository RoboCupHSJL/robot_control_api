from .camera_interface import CameraInterface
import logging

class TestCamera(CameraInterface):
    def __init__(self, name, agent, config, clock):
        super().__init__(name, config, clock)

    def start(self):
        try:
            self.status = 'enabled'
        except Exception as start_exception:
            self.status = 'disabled'
            logging.error(start_exception)

    def _get_image(self):
        logging.debug("TEST CAMERA GET IMAGE CALLED")
        return None

    def _get_height(self):
        logging.debug("TEST CAMERA GET HEIGHT CALLED")
        return None

    def _get_width(self):
        logging.debug("TEST CAMERA GET WDITH CALLED")
        return None

    def _get_encoding(self):
        logging.debug("TEST CAMERA GET ENCODING CALLED")
        return None