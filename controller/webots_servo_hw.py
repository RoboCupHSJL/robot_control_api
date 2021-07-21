from servo_actuator_interface import ServoActuatorInterface

class WebotsServoHW(ServoActuatorInterface):
    def __init__(self, name):
        self._name = name
        wb_device = None # IMPORT FROM CONTROLLER
        self.__position_sensor = wb_devices[0]
        self.__motor = wb_devices[1]

    def start(self):
        try:
            self.__position_sensor.enable()
            self.__motor.enable()
        except:
            self._status = 'disabled'
            return

        self._status = 'enabled'

    def _get_position(self):
        #if self.__position_sensor:
        #    return self.__position_sensor.getValue()
        #else:
        #    return None
        return self.__current_position

    def _set_position(self, request, response):
        ang = request.value
        #self.__motor.setPosition(ang)
        #response.success = True
        #return response
        self.__current_position = ang
