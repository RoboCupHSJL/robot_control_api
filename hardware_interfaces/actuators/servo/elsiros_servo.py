from .servo_interface import ServoInterface


class ElsirosServo(ServoInterface):
    """[summary]

    Args:
        ServoInterface ([type]): [description]
    """
    def __init__(self, name, agent):
        super().__init__(name)
        self.agent = agent
        #self.__posititon_sensor = self.robot.servos[self._name + '_sensor']
        #self.__motor = self.robot.servos[self._name]

    def start(self):
        try:
            self._status = 'enabled'
        except:
            self._status = 'disabled'
            return


    def _get_position(self):
        try:
            self.agent.get_position()
        except:
            return None

    def _set_position(self, ang):
        try:
            self.agent._set_position(ang)
        except:
            return None
