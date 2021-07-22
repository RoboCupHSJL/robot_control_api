from position_controller_interface import PositionControllerInterface
from controller_interface import ControllerInterface
from webots_servo_hw import WebotsServoHW

class WebotsPositionController(PositionControllerInterface):
    def __init__(self, name, robot):
        super().__init__(name)

        self.robot = robot

        self._add_interface(WebotsServoHW('head_yaw', robot))

    def step(self):
        super().step()
        self.hw_list['head_yaw'].write(1.0)
