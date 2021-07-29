from controllers import WebotsPositionController
from controllers import WebotsImuController
from controllers import WebotsCameraController

from controller import Robot

class ControllerManager:
    def __init__(self, type, robot=None):

        self.controllers = {}
        if type == 'Webots':
            self.robot = robot
            self.__init_webots(robot)

    def __init_webots(self, robot): 
        self.controllers['imu'] = WebotsImuController('imu_controller', robot)
        self.controllers['servos'] = WebotsPositionController('servos_controller', robot)
        self.controllers['camera'] = WebotsCameraController('camera_controller', robot)

    def _step(self):
        for controller in self.controllers:
            self.controllers[controller].step()

    def start(self):
        while True:
            self.robot.step(100)
            self._step()
