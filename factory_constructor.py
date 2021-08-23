from controllers.camera_controllers.factory_camera_controller \
    import GeneralCameraController
from controllers.imu_controllers.factory_imu_controller \
    import GeneralImuController
from controllers.servo_controllers.factory_position_controller \
    import GeneralPositionController

class FactoryConstructor:
    def __init__(self, control_config, mode):
        self.controllers = {}

        self.agent = None

        if mode == 'webots':
            from controller import Robot
            self.agent = Robot()
        elif mode == 'elsiros':
            from elsiros_communicator import ElsirosCommunicator
            self.agent = ElsirosCommunicator()
        else:
            # IMPORT AND ASSIGNMENT OF THE CUSTOM AGENT 
            pass
        self.agent.enable()

        self.controllers['imu'] = GeneralImuController('imu_controller', self.agent, mode)
        self.controllers['servos'] = GeneralPositionController('servo_controller', 
                                                               control_config.get('servo_controller'), 
                                                               self.agent,
                                                               mode)
        self.controllers['camera'] = GeneralCameraController('camera_controller', self.agent, mode)
            
        


