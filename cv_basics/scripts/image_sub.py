#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def callback(data):
	br = CvBridge()
	rospy.loginfo('RECEIVING')
	img = br.imgmsg_to_cv2(data)
	cv2.imwrite('SavedImg.jpg',img)
	cv2.waitKey(1)
	cv2.destroyAllWindows()

def receive_msg():
	rospy.init_node('Image_sub')
	rospy.Subscriber('imageframe', Image, callback)

if __name__ == "__main__":
	receive_msg()
	rospy.spin()
