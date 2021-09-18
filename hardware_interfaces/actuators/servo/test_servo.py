from .servo_interface import ServoInterface
import logging


class TestServo(ServoInterface):
    """[summary]

    Args:
        ServoInterface ([type]): [description]
    """
    def __init__(self, name, agent, config, clock):
        super().__init__(name, config, clock)

    def start(self):
        try:
            self._status = 'enabled'
        except:
            self._status = 'disabled'
            return


    def _get_position(self):
        logging.debug('TEST SERVO GET POSITION CALLED')
        return None

    def _set_position(self, ang):
        logging.debug('TEST SERVO SET POSITION CALLED')