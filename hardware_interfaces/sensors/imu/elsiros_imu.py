# TODO: add docs
# TODO: add config read
import logging
from .imu_interface import IMUSensorInterface


class ElsirosIMU(IMUSensorInterface):
    """[summary]

    Args:
        IMUSensorInterface ([type]): [description]
    """

    def __init__(self, name, robot):
        super().__init__(name)
        self.robot = robot

    def get_param(self, param_name):
        pass

    def start(self):
        try:
            self.robot.imu.enable(100) # ?????
            self.status = 'enabled'
        except Exception as start_exception:
            self.status = 'disabled'
            logging.error(start_exception)

        self.status = 'enabled'

    def _get_orientation(self):
        orientation = None
        if self.status == 'enabled':
            orientation = self.robot.imu.getRollPitchYaw()
        else:
            logging.error("IMU is not started")
        return orientation