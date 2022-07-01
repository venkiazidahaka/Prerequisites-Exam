#!/usr/bin/env python

from robot_control_class import RobotControl


class ExamControl():
    def __init__(self):
        self.rc = RobotControl()
        self.inf = float("inf")

    def get_laser_readings(self):
        right = self.rc.get_laser(0)
        left = self.rc.get_laser(719)

        return left, right

    def main(self):
        left, right = self.get_laser_readings()
        while left != self.inf or right != self.inf:
            self.rc.move_straight()
            left, right = self.get_laser_readings()
            print(left, right)
        self.rc.stop_robot()
