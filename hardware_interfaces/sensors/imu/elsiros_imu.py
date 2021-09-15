# TODO: add docs
# TODO: add config read
import logging
from .imu_interface import IMUSensorInterface


class ElsirosIMU(IMUSensorInterface):
    """[summary]

    Args:
        IMUSensorInterface ([type]): [description]
    """

    def __init__(self, name, agent, config, clock):
        super().__init__(name, config, clock)
        self.agent = agent

    def get_param(self, param_name):
        pass

    def start(self):
        try:
            self.status = 'enabled'
            self.agent.sensors[self.name] = 100
        except Exception as start_exception:
            self.status = 'disabled'
            logging.error(start_exception)

        self.status = 'enabled'

    def _get_orientation(self):
        orientation = None
        if self.status == 'enabled':
            orientation = self.agent.get_data(self.name)
            #logging.debug(orientation)
        else:
            logging.error("IMU is not started")
        return orientation