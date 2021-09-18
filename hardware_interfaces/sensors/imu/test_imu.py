import logging
from .imu_interface import IMUSensorInterface


class TestIMU(IMUSensorInterface):
    """[summary]

    Args:
        IMUSensorInterface ([type]): [description]
    """

    def __init__(self, name, agent, config, clock):
        super().__init__(name, config, clock)

    def get_param(self, param_name):
        pass

    def start(self):
        try:
            self.status = 'enabled'
        except Exception as start_exception:
            self.status = 'disabled'
            logging.error(start_exception)

        self.status = 'enabled'

    def _get_orientation(self):
        logging.debug('TEST IMU GET ORIENTATION CALLED')
        return None