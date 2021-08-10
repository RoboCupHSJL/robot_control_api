# TODO: add docs
import logging
from .servo_interface import ServoInterface
from controller import PositionSensor, Motor


class WebotsServo(ServoInterface):
    """[summary]

    Args:
        ServoInterface ([type]): [description]
    """
    def __init__(self, name, agent):
        super().__init__(name)
        self.__robot = agent
        self.__position_sensor = PositionSensor(name + '_sensor')
        #self.__position_sensor.enable(100)
        self.__motor = Motor(name)

    def get_param(self, param_name):
        result = None
        return result

    def start(self):
        try:
            self.__position_sensor.enable(100)
            #self.__motor.enable()
        except Exception as e:
            self.status = 'disabled'
            logging.error("Couldn't start servo interface %s. Exception is %s",
                          self.name, e)

        self.status = 'enabled'

    def _get_position(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        current_position = None
        if self.status == 'enabled':
            current_position = self.__position_sensor.getValue()
        else:
            logging.error("Servo interface %s is not enabled", self.name)
        return current_position

    def _set_position(self, goal_position):
        """[summary]

        Args:
            ang ([type]): [description]
        """
        self.__motor.setPosition(goal_position)
