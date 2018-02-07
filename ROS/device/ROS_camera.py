#!/usr/bin/env python3

import rospy
import time
import threading
import os
import glob
import sys
sys.path.append(“/opt/ros/kinetic/lib/python2.7/dist-packages”)
import cv2
import numpy
import camera

from PIL import Image
im = Image
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from necst.msg import oneshot_msg

class camera_con(object):
    filename = ‘’
    filesize = 1

    def __init__(self):
        #camera = camera.controller()
        #camera.detect_camera()
        #camera.setwhitebalance(white=’SKY’)
        #camera.set_crop(crop=‘1.3x’)
        pass

    def start_thread(self):
        th = threading.Thread(target = self.pub_image)
        th.setDaemon(True)
        th.start()
        return

    def shutter(self, req):
        self.filename = req.filename
        self.filesize = req.filesize
        print(req)
        while True:
            if not self.filename == ‘’:
                break
            print(‘please filename!’)
        #image = cam.shutter_download(filename=self.filename)
        self.pub_image()
        print(‘shoot’+self.filename)
        return

    def pub_image(self):
        while True:
            if os.path.exists(self.filename) == True:
                break
            time.sleep(0.1)
        print(“$$$$$$$$$$$$”)
        img = cv2.imread(self.filename, 1)
        bridge = CvBridge()
        pub = rospy.Publisher(‘Image’, Image, queue_size = 100, latch = True)

        while not rospy.is_shutdown():
            pub.publish(bridge.cv2_to_imgmsg(omg, ‘bgr8’))
            print(‘publish’)
            time.sleep(0.5)
        return

if __name__ == ‘__main__’:
    cam = camera_con()
    rospy.init_node(‘camera_controller’)
    rospy.loginfo(‘waiting publish camera’)
    cam.start_thread()
    sub = rospy.Subscriber(‘oneshot’, oneshot_msg, cam.shutter)
    rospy.spin()
 