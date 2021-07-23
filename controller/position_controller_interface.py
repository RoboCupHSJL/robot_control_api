from controller_interface import ControllerInterface
import queue

class PositionControllerInterface(ControllerInterface):
    def __init__(self, name):
        super().__init__(name)
        self._pos_queue = queue.Queue()

        self._servo_id_list = ['head_yaw', 
                    'head_pitch', 
                    'left_shoulder_pitch', 
                    'left_shoulder_roll', 
                    'left_shoulder_twirl', 
                    'left_elbow_pitch', 
                    'left_hand_twirl', 
                    'left_finger_pitch', 
                    'right_shoulder_pitch', 
                    'right_shoulder_roll', 
                    'right_shoulder_twirl', 
                    'right_elbow_pitch', 
                    'right_hand_twirl', 
                    'right_finger_pitch', 
                    'pelvis_pitch', 
                    'left_hip_yaw', 
                    'left_hip_roll', 
                    'left_hip_pitch', 
                    'left_knee', 
                    'left_ankle_pitch', 
                    'left_ankle_roll', 
                    'right_hip_yaw', 
                    'right_hip_roll', 
                    'right_hip_pitch', 
                    'right_knee', 
                    'right_ankle_pitch', 
                    'right_ankle_roll']

    def step(self):
        super().step()
        if not self._pos_queue.empty():
            servo_name, position = self._pos_queue.get()
            self.hw_list[servo_name].write(position)

    def set_position(self, servo_name, position):
        self._pos_queue.put([servo_name, position])
        
        
    def command_callback(self, msg):
        self.queue.push(msg)
