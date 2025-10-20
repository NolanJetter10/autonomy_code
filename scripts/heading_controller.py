#!/usr/bin/env python3

import numpy as np
import rclpy

from asl_tb3_lib.control import BaseHeadingController
from asl_tb3_lib.math_utils import wrap_angle
from asl_tb3_msgs.msg import TurtleBotControl, TurtleBotState


class HeadingController(BaseHeadingController):
    def __init__(self):
        super().__init__()
        
        self.declare_parameter("kp", 2.0)
    
    @property
    def kp(self) -> float:
        return self.get_parameter("kp").value
    
    def compute_control_with_goal(self, current_state: TurtleBotState, desired_state: TurtleBotState) -> TurtleBotControl:
        error = wrap_angle(desired_state.theta - current_state.theta)
        omega = self.kp * error
        control = TurtleBotControl()
        control.v = 0.0
        control.omega = omega
        
        return control
        

if __name__ == "__main__":
    rclpy.init()
    controller = HeadingController()
    rclpy.spin(controller)
    rclpy.shutdown()
    