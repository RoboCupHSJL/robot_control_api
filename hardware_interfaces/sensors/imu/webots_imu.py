# TODO: add docs
# TODO: add config read
import logging
from .imu_interface import IMUSensorInterface
from controller import InertialUnit


class WebotsIMU(IMUSensorInterface):
    """[summary]

    Args:
        IMUSensorInterface ([type]): [description]
    """

    def __init__(self, name, agent, config, clock):
        super().__init__(name, config, clock)
        self.agent = agent

        self.__in_unit = InertialUnit(self.name)

    def get_param(self, param_name):
        pass

    def start(self):
        try:
            self.__in_unit.enable(100)
            self.status = 'enabled'
        except Exception as start_exception:
            self.status = 'disabled'
            logging.error(start_exception)

        self.status = 'enabled'

    def _get_orientation(self):
        orientation = None
        if self.status == 'enabled':
            orientation = self.__in_unit.getRollPitchYaw()
        else:
            logging.error("IMU is not started")
        return orientation
