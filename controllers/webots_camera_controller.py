from .camera_controller_interface import CameraControllerInterface
from hardware_interfaces.sensors import WebotsCamera


class WebotsCameraController(CameraControllerInterface):
    def __init__(self, name, robot):
        super().__init__(name)

        self.robot = robot

        self._add_interface(WebotsCamera(name='camera', robot=robot))

    def step(self):
        super().step()
