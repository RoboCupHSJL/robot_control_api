from hw_interface import HWInterface

class ActuatorInterface(HWInterface):
    def __init__(self, name):
        super().__init__(name)

    def read(self):
        raise NotImplementedError

    def write(self):
        raise NotImplementedError