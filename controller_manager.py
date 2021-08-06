# TODO: add docs
from controllers import WebotsPositionController
from controllers import WebotsImuController
from controllers import WebotsCameraController

from controller import Robot


class ControllerManager:
    """[summary]
    """
    def __init__(self, case, robot=None):

        self.controllers = {}
        if case == 'Webots':
            self.robot = robot
            self.__init_webots(robot)

    def __init_webots(self, robot):
        """[summary]

        Args:
            robot ([type]): [description]
        """
        self.controllers['imu'] = WebotsImuController('imu_controller',
                                                      robot)
        self.controllers['servos'] = WebotsPositionController('servos_controller', robot)
        self.controllers['camera'] = WebotsCameraController('camera_controller', robot)

    def __step(self):
        """[summary]
        """
        for controller in self.controllers:
            self.controllers[controller].step()

    def start(self):
        """[summary]
        """
        for controller in self.controllers:
            self.controllers[controller].start()
        while True:
            self.robot.step(100)
            self.__step()
