from servo_interface import ServoInterface


class ElsirosServo(ServoInterface):
    """[summary]

    Args:
        ServoInterface ([type]): [description]
    """
    def __init__(self, name, robot):
        self._name = name
        self.robot = robot
        self.__posititon_sensor = self.robot.servos[self._name + '_sensor']
        self.__motor = self.robot.servos[self._name]

    def start(self):
        try:
            self.__posititon_sensor.enable(100)
            self.__motor.enable()
        except:
            self._status = 'disabled'
            return

        self._status = 'enabled'

    def _get_position(self):
        if self.__position_sensor:
            return self.__position_sensor.getValue()
        else:
            return None

    def _set_position(self, ang):
        #ang = request.value
        self.__motor.setPosition(ang)
        return
