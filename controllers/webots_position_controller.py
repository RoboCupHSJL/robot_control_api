from position_controller_interface import PositionControllerInterface
from controller_interface import ControllerInterface
from webots_servo_hw import WebotsServoHW

class WebotsPositionController(PositionControllerInterface):
    def __init__(self, name, robot):
        super().__init__(name)

        self.robot = robot

        for servo_name in self._servo_id_list:
            self._add_interface(WebotsServoHW(servo_name, robot))

        #self._add_interface(WebotsServoHW('head_yaw', robot))

    def step(self):
        super().step()
