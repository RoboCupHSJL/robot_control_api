import rclpy
from rclpy.node import Node

class ControllerInterface(Node):
    def __init__(self, name):
        super().__init__(name)
        self.hw_list = {}

    def step(self):
        pass

    def start(self):
        for hw in self.hw_list:
            self.hw_list[hw].start()

    def stop(self):
        pass

    def _add_interface(self, hw):
        self.hw_list[hw.get_name] = hw

