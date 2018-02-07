#!/usr/bin/env python3

import rospy
import sys
sys.path.append("/opt/ros/kinetic/lib/python2.7/dist-packages")
import time
import threading

from necst.msg import oneshot_msg

class oneshot(object):
    
    def __init__(self):
        rospy.init_node('oneshot')
        self.pub = rospy.Publisher('oneshot', oneshot_msg, queue_size=10, latch =True)
        return

    def oneshot(self, filename, filesize=1):
        # filesize = 1 or 2 
        msg = oneshot_msg()
        msg.filename = filename
        msg.filesize = filesize
        while not rospy.is_shutdown():
            self.pub.publish(msg)
            rospy.loginfo(filename)
            time.sleep(0.5)
        return