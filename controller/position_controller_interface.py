from controller_interface import ControllerInterface

class PositionControllerInterface(ControllerInterface):
    def __init__(self):
        pass

    def step(self):

        for hw in self.hw_list:
            hw.publish()

        for command in self.queue.pop():
            try:
                self.hw_list[command.name].write(command.value)
            except KeyError:
                raise Exception('Non existant servo name in the massage')
        
    def command_callback(self, msg):
        self.queue.push(msg)
