from elsiros_webots.controllers.player.elsiros_communication import CommunicationManager

class ElsirosCommunicator:
    def __init__(self):
        self.cm = CommunicationManager()
        self.frame = {}
        self.__enabled = False
        self.sensors = {}
        self.__curr_time = None

    def enable(self):
        self.__enabled = True

    def start(self):
        assert self.__enabled, "communicator is not enabled"
        self.cm.enable_sensors(self.sensors)
        print(self.sensors)
        self.cm.execute()

    def step(self, rate):
        assert self.__enabled, "communicator is not enabled"
        self.cm.add_to_queue(self.frame)
        self.__curr_time = self.cm.getTime()

    def set_position(self, name, value):
        assert self.__enabled, "communicator is not enabled"
        self.frame[name] = value

    def get_data(self, name):
        assert self.__enabled, "communicator is not enabled"
        return self.cm.get_sensor(name)

    def get_time(self):
        return self.__curr_time