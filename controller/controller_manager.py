from webots_imu_controller import WebotsImuController
import rclpy
from rclpy.node import Node
from controller import Robot

class ControllerManager:
    def __init__(self, type):

        self.controllers = {}
        if type == 'Webots':
            self.__init_webots()

    def __init_webots(self):
        robot = Robot()
        self.controllers['imu'] = WebotsImuController('imu_controller', robot)

    def step(self):
        print('manager_step')
        for controller in self.controllers:
            self.controllers[controller].step()
