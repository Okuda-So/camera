#!/usr/bin/env python3

import time
import threading
import rospy
import numpy
import cv2
import sys
sys.path.append("/home/amigos/ros/src/necst/lib")

from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from necst.msg import oneshot_msg

class Image(object):

    filename = ''

    def __init__(self):
        pass

    def start_thread(self):
        th1 = threading.Thread(target = self.Image_view)
        th1.setDaemon(True)
        th1.start()
        th2 = threading.Thread(target = self.dec_filename)
        th2.setDaemon(True)
        th2.start()
        return

    def Image_view(self, req):
        bridge = CvBridge()
        print(req)
        img_data = bridge.imgmsg_to_cv2(req, 'bgr8')
        img = cv2.imread(self.filename, 1)
        cv2.imshow(self.filename, img_data)
        print(‘push [s]key to preserve image’)
        If cv2.waitKey(0) == ord(’s’):
            cv2.imwrite(self.filename, img)
            cv2.destroyAllWindows()
        self.filename = ''
        return

    def dec_filename(self, req):
        req.data = self.filename
        return

if __name__ == '__main__':
    Image = Image()
    rospy.init_node('Image')
    Image.start_thread()
    sub = rospy.Subscriber('Image', Image, Image.Image_view)
    sub = rospy.Subscriber('oneshot', oneshot_msg, Image.dec_filename)
    rospy.spin()
