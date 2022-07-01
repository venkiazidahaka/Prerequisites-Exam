#!/usr/bin/env python

from robot_control_class import RobotControl


def get_highest_lowest():
    rc = RobotControl()
    d_list = rc.get_laser_full()
    new_list = []
    inf = float("inf")
    for x in d_list:
        if x != inf:
            new_list.append(x)
    # print(new_list)
    max_dist = max(new_list)
    min_dist = min(new_list)
    max_dist_pos = d_list.index(max_dist)
    min_dist_pos = d_list.index(min_dist)
    print(max_dist_pos)
    print(min_dist_pos)
    return max_dist_pos,min_dist_pos

