from hw_interface import HWInterface

class SensorInterface(HWInterface):
    def __init__(self, name):
        super().__init__(name)

    def read(self):
        pass
