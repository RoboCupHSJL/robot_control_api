from elsiros_communication import CommunicationManager

class ElsirosCommunicator:
    def __init__(self):
        self.cm = CommunicationManager()
        self.frame = {}
        self.__enabled = False

    def enable(self):
        self.__enabled = True

    def start(self, sensors):
        assert self.__enabled, "communicator is not enabled"
        self.cm.enable_sensors(sensors)

    def step(self):
        assert self.__enabled, "communicator is not enabled"
        self.cm.add_to_queue(self.frame)

    def set_position(self, name, value):
        assert self.__enabled, "communicator is not enabled"
        self.frame[name] = value

    def get_data(self, name):
        assert self.__enabled, "communicator is not enabled"
        return self.cm.get_sensor(name)