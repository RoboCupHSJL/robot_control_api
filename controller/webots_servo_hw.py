from servo_actuator_interface import ServoActuatorInterface
from controller import PositionSensor, Motor

class WebotsServoHW(ServoActuatorInterface):
    def __init__(self, name, robot):
        self._name = name
        self.robot = robot
        wb_device = None # IMPORT FROM CONTROLLER
        self.__position_sensor = PositionSensor(name + '_sensor')
        self.__position_sensor.enable(100)
        self.__motor = Motor(name)
        

    def start(self):
        try:
            self.__position_sensor.enable(100)
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
