# TODO: add docs
# TODO: add config read
import logging
from .imu_interface import IMUSensorInterface


class ElsirosIMU(IMUSensorInterface):
    """[summary]

    Args:
        IMUSensorInterface ([type]): [description]
    """

    def __init__(self, name, agent):
        super().__init__(name)
        self.agent = agent

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
        orientation = None
        if self.status == 'enabled':
            self.agent.get_pitch_roll_yaw()
        else:
            logging.error("IMU is not started")
        return orientation