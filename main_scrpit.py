from controller_manager import ControllerManager
from controller import Robot


kondo_webots_cm = ControllerManager()
kondo_webots_cm.controllers['servos'].set_position('head_yaw', -0.5)
kondo_webots_cm.controllers['servos'].set_position('head_pitch', 0.5)

kondo_webots_cm.start()

# while True:
#    for controller in kondo_webots_cm.controllers:
#        rclpy.spin_once(kondo_webots_cm.controllers[controller])
#        kondo_webots_cm.controllers[controller].step()
