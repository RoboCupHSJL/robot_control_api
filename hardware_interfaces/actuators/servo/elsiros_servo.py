from .servo_interface import ServoInterface
import logging


class ElsirosServo(ServoInterface):
    """[summary]

    Args:
        ServoInterface ([type]): [description]
    """
    def __init__(self, name, agent, config, clock):
        super().__init__(name, config, clock)
        self.agent = agent
        #self.__posititon_sensor = self.robot.servos[self._name + '_sensor']
        #self.__motor = self.robot.servos[self._name]

    def start(self):
        try:
            self._status = 'enabled'
            self.agent.sensors[self.name] = 100
        except:
            self._status = 'disabled'
            return


    def _get_position(self):
        position = None
        if self.status == 'enabled':
            position = self.agent.get_data(self.__name)
            #logging.debug(position)
        else:
            logging.error(self.name, " servo is not started")
        return position

    def _set_position(self, ang):
        try:
            self.agent.set_position(self.__name, ang)
        except:
            return None
