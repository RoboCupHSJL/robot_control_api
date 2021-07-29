from controller_interface import ControllerInterface

class CameraControllerInterface(ControllerInterface):
    def __init__(self, name):
        super().__init__(name)

    def _read(self, msg_type):
        pass

    def start(self):
        super().start()

    def step(self):
        super().step()
        for hw_name in self.hw_list:
            self.hw_list[hw_name].publish()
