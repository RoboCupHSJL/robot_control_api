from controller_manager import ControllerManager
from controller import Robot
from messages.servo_cmd_message import ServoCmdMessage
from communication import interactor


kondo_webots_cm = ControllerManager()
cmd_msg = ServoCmdMessage()
cmd_msg.frame = {'head_yaw' : -0.5,
                 'head_pitch' : 0.5}

interactor.push_message('servo_cmd', cmd_msg)

kondo_webots_cm.start()

# while True:
#    for controller in kondo_webots_cm.controllers:
#        rclpy.spin_once(kondo_webots_cm.controllers[controller])
#        kondo_webots_cm.controllers[controller].step()
