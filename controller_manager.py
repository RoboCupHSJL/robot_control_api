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

from factory_constructor import FactoryConstructor



class ControllerManager:
    """[summary]
    """
    def __init__(self):
        self.controllers = {}
        self.__agent = None
        self.__running = False

        FC = FactoryConstructor(control_config, CONTROL_MODE)

        self.__agent = FC.agent
        self.controllers['imu'] = FC.controllers['imu']
        self.controllers['servos'] = FC.controllers['servos']
        self.controllers['camera'] = FC.controllers['camera']

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
        self.__agent.start()
        while self.__running:
            self.__step()

    def stop(self):
        """[summary]
        """
        self.__running = False
        for controller in self.controllers:
            self.controllers[controller].stop()
