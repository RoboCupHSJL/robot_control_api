# TODO: add docs
# TODO: add config read
import logging
from .camera_interface import CameraInterface


class ElsirosCamera(CameraInterface):
    """[summary]

    Args:
        CameraInterface ([type]): [description]
    """

    def __init__(self, name, agent, config, clock):
        super().__init__(name, config, clock)
        self.agent = agent


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
            self.status = 'enabled'
            self.agent.sensors[self.name] = 100
        except Exception as start_exception:
            self.status = 'disabled'
            logging.error(start_exception)

    def _get_image(self):
        image = None
        if self.status == 'enabled':
            image = self.agent.get_data(self.name)
        else:
            logging.error("Camera is not started")
        return image

    def _get_height(self):
        height = 240
        ##if self.status == 'enabled':
        #    self.agent.get_data(self.name)['height']
        #else:
        #    logging.error("Camera is not started")
        return height

    def _get_width(self):
        width = 320
        #if self.status == 'enabled':
        #    self.agent.get_data(self.name)['width']
        #else:
        #    logging.error("Camera is not started")
        return width

    def _get_encoding(self):
        return "bgra8"
