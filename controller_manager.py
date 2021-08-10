# TODO: add docs
import os
import json
import logging

# ===========================CONFIG-READING-STUFF==============================
# =============================================================================
logging_levels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

with open(os.path.join("config", "main.json")) as main_config_file:
    main_config = json.load(main_config_file)

with open(os.path.join("config",
                       main_config.get('control_config_file'))) \
                            as control_config_file:
    control_config = json.load(control_config_file)

LOGING_LEVEL = main_config.get('logging_level')
assert isinstance(LOGING_LEVEL, str), "logging_level should be a string"

if LOGING_LEVEL in logging_levels:
    logging.basicConfig(level=logging_levels[LOGING_LEVEL])
else:
    raise ValueError(
        "Config error. \
        Logging level could be only:\nDEBUG\nINFO\nWARNING\nERROR\nCRITICAL")

CONTROL_MODE = control_config.get('mode')

#print(control_config.get('servo_controller').get('servos').items())

assert isinstance(CONTROL_MODE, str), "mode should be a string"

# =============================================================================
# =============================================================================

# write here nessesary imports for the control mode
if CONTROL_MODE == 'webots':
    from controllers.servo_controllers.webots_position_controller \
        import WebotsPositionController
    from controllers.imu_controllers.webots_imu_controller \
        import WebotsImuController
    from controllers.camera_controllers.webots_camera_controller \
        import WebotsCameraController
    from controller import Robot
elif CONTROL_MODE == 'elsiros':
    from controllers.servo_controllers.elsiros_position_controller \
        import ElsirosPositionController
    from controllers.camera_controllers.elsiros_camera_controller \
        import ElsirosCameraController
    from controllers.imu_controllers.elsiros_imu_controller \
        import ElsirosImuController
    from elsiros_communicator import ElsirosCommunicator


class ControllerManager:
    """[summary]
    """
    def __init__(self):
        self.controllers = {}
        self.__agent = None
        self.__running = False
        if CONTROL_MODE == 'webots':
            self.__agent = Robot()
            self.__init_webots(self.__agent)
        elif CONTROL_MODE == 'elsiros':
            self.__agent = ElsirosCommunicator()
            self.__init_elsiros(self.__agent)

    def __init_webots(self, agent):
        """[summary]

        Args:
            robot ([type]): [description]
        """
        self.controllers['imu'] = WebotsImuController('imu_controller', agent)
        self.controllers['servos'] = WebotsPositionController('servo_controller', 
                                                              control_config.get('servo_controller'), 
                                                              agent)
        self.controllers['camera'] = WebotsCameraController('camera_controller', agent)

    def __init_elsiros(self, agent):
        """[summary]

        Args:
            robot ([type]): [description]
        """
        self.controllers['imu'] = ElsirosImuController('imu_controller', agent)
        self.controllers['servos'] = ElsirosPositionController('servos_controller', 
                                                               control_config.get('servo_controller'), 
                                                               agent)
        self.controllers['camera'] = ElsirosCameraController('camera_controller', agent)

    def __step(self):
        """[summary]
        """
        for controller in self.controllers:
            self.controllers[controller].step()
        #if self.__agent is not None and self.__agent.__hasattr__("step"):
        #    self.__agent.step(control_config.get("agent_rate"))
        if self.__agent is not None and hasattr(self.__agent, "step"):
            self.__agent.step(control_config.get("agent_rate"))

    def start(self):
        """[summary]
        """
        self.__running = True
        for controller in self.controllers:
            self.controllers[controller].start()
        while self.__running:
            self.__step()

    def stop(self):
        """[summary]
        """
        self.__running = False
        for controller in self.controllers:
            self.controllers[controller].stop()
