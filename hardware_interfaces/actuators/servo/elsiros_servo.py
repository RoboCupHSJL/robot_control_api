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
            self.agent.sensors[self.name] = 100
        except:
            self._status = 'disabled'
            return


    def _get_position(self):
        position = None
        try:
            position = self.agent.get_data(self.__name)
        except:
            pass
        return position

    def _set_position(self, ang):
        try:
            self.agent.set_position(self.__name, ang)
        except:
            return None
