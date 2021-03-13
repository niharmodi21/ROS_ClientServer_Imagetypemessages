#!/usr/bin/env python3

import rospy
from cv_bridge import CvBridge
import cv2
from image_msgs.msg import HS

def publish_msg():
	pub = rospy.Publisher('imageframe',HS, queue_size=10)
	rospy.init_node('Image_pub')
	rate = rospy.Rate(1)
	image = cv2.imread('/home/chirag/LAIR.jpg')
	br = CvBridge()
	rospy.loginfo('PUBLISHING')
	image1 = br.cv2_to_imgmsg(image)
	msg = HS()
	msg.name = 'Nihar'
	msg.img = image1
	pub.publish(msg)
	rate.sleep()

if __name__ == "__main__":
	publish_msg()
	rospy.spin()
