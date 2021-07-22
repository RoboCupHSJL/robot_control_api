from controller_interface import ControllerInterface

class PositionControllerInterface(ControllerInterface):
    def __init__(self, name):
        super().__init__(name)

    def step(self):
        super().step()

    def set_position(self, servo, position):
        self.hw_list[servo].write(position)
        
        
    def command_callback(self, msg):
        self.queue.push(msg)
