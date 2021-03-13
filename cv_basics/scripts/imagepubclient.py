#!/usr/bin/env python3

import rospy
from image_msgs.srv import sendimage
from cv_bridge import CvBridge
import cv2
import os

if __name__ == '__main__':
	rospy.init_node('Publish_client')
	rospy.wait_for_service("/pubimage")
	
	try:
		pubimage = rospy.ServiceProxy("/pubimage", sendimage)
		response = pubimage('YES')
		rospy.loginfo("Image Received:")
		rospy.loginfo(str(response.im))
		br = CvBridge()
		image = br.imgmsg_to_cv2(response.im)
		cv2.imwrite(r'/home/chirag/abc.jpg', image)
		
	except rospy.ServiceException as e:
		rospy.logwarn("service failed: " + str(e))
