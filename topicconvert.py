#!/usr/bin/env python  
#coding=utf-8
import rospy  
from sensor_msgs.msg import Image  
from cv_bridge import CvBridge, CvBridgeError  
import cv2  
import numpy as np  
  
class ImageConverterNode:  
    def __init__(self):  
        # 初始化ROS节点  
        rospy.init_node('hy', anonymous=True)  
          
        # 创建发布者，发布灰度图像  
        self.pub = rospy.Publisher('/cam0/image_raw/gray', Image, queue_size=10)  
          
        # 创建转换器对象  
        self.bridge = CvBridge()
          
        # 订阅BGR8图像  
        rospy.Subscriber('/cam0/image_raw', Image, self.image_callback)  
      
    def image_callback(self, msg): 
        # 将BGR8图像转换为灰度图像  
        try:  
            timestamp = rospy.Time().now().to_sec()  
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')  
            gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)  
              
            # 将灰度图像转换为ROS图像消息并发布  
            ros_image = self.bridge.cv2_to_imgmsg(gray_image, 'mono8')  
            ros_image.header.stamp = rospy.Time.from_sec(timestamp) 
            self.pub.publish(ros_image)  
        except CvBridgeError as e:  
            print(e)
      
if __name__ == '__main__':  
    try:  
        node = ImageConverterNode()  
        rospy.spin()  
    except rospy.ROSInterruptException:  
        pass