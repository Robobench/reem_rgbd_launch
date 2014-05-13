#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on May 13 2014

@author: Sam Pfeiffer

Set dynamic params for the simulated Xtion of REEM.
We must lower the quantity of data sent.


"""

import rospy
from dynamic_reconfigure import client, DynamicReconfigureParameterException


if __name__=='__main__':
    rospy.init_node("set_simulated_xtion_dyn_params", anonymous=True)
    rospy.loginfo("Trying to connect a service client to head_mount_xtion dynamic reconfigure...")
    client = client.Client("/head_mount_xtion")
    rospy.loginfo("Got a client! Setting parameters.")
    try:
        config = client.update_configuration({'imager_rate' : 1.0})
    except DynamicReconfigureParameterException:
        rospy.sleep(5)  # Giving some time to catch up with simulation startup
        config = client.update_configuration({'imager_rate' : 1.0})

    # check if it was really set
    
    rospy.loginfo("Parameters set: " + str(config))

