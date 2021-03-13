#!/usr/bin/env python3

import rospy
from image_msgs.srv import sendimage
from cv_bridge import CvBridge
import cv2
import os

def handle(req):
	if req.request == "YES":
		image = cv2.imread('/home/chirag/LAIR.jpg')
		br = CvBridge()
		rospy.loginfo('DONEG')
		image1 = br.cv2_to_imgmsg(image)
		return image1
		
if __name__ == "__main__":
	rospy.init_node("Publish_Server")
	rospy.loginfo("SERVER NODE CREATED")
	service = rospy.Service("/pubimage", sendimage, handle)
	rospy.loginfo("SERVER STARTED")
	rospy.spin()
