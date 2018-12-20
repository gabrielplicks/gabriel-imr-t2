#!/usr/bin/env python

import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

class TurtlebotEdgeDetector:
  def __init__(self):
    """ interface between ros and opencv """
    self.bridge = cv_bridge.CvBridge()
    cv2.namedWindow("window", 1)
    # cv2.namedWindow("image", 2)

    # Subscribe to ROS topics
    self.image_sub = rospy.Subscriber('camera/rgb/image_raw', Image, self.image_callback)

  def image_callback(self, msg):
    # Reads the image from camera topic and transform to OpenCV format
    image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
    
    # Apply canny edge detector with thresholds
    edges = cv2.Canny(image, 20, 100)

    cv2.imshow("window", edges)
    # cv2.imshow("window", image)
    cv2.waitKey(3)

rospy.init_node('turtlebot_edge_detector')
turtlebot_edge_detector = TurtlebotEdgeDetector()
rospy.spin()