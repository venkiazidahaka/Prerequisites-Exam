#!/usr/bin/env python

from robot_control_class import RobotControl
from math import radians


def robot_movement():
    rc = RobotControl()
    distance = rc.get_front_laser()
    while distance > 1:
        distance = rc.get_front_laser()
        rc.move_straight()
        print(distance)

    rc.stop_robot()
    rc.turn(clockwise="clockwise", speed=radians(90), time=1)


if __name__ == "__main__":
    robot_movement()
