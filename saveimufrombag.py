#coding=utf-8
import rosbag
import rospy
from sensor_msgs.msg import Imu
import sys
import os

# bag = rosbag.Bag('/media/hy/B0CC6321622802A9/ORB-Exp/XTDrone/Seq005/2023-11-28-12-47-16.bag', 'r')
bag_path = sys.argv[1]
topic_name = sys.argv[2]
# out_path = bag_path[:bag_path.rfind(os.path.sep)]+"/imu.csv"
out_path = sys.argv[3]

fout = open(out_path, "w")

with rosbag.Bag(bag_path, 'r') as bag:  #要读取的bag文件；
    for topic,msg,t in bag.read_messages():
        if topic == topic_name: #图像的topic；  
            # try:
                # cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
            # except CvBridgeError as e:
            #     print(e)
            timestr = "%.6f" %  msg.header.stamp.to_sec()
            #%.6f表示小数点后带有6位，可根据精确度需要修改；
            timestr = '{:.0f}'.format(float(timestr)*1000000000)
            print(timestr)
            # print(msg.angular_velocity.x, msg.angular_velocity.y, msg.angular_velocity.z)
            fout.write(timestr + "," + str(msg.angular_velocity.x) + "," + str(msg.angular_velocity.y) + "," + str(msg.angular_velocity.z) +"," + str(msg.linear_acceleration.x) + "," + str(msg.linear_acceleration.y) + "," + str(msg.linear_acceleration.z) + "\n")

fout.close()

# (header, imu_data) = bag.read_messages(['/iris_0/imu_gazebo'])
# print(imu_data.header.stamp ,imu_data.angular_velocity.x, imu_data.angular_velocity.y, imu_data.angular_velocity.z, imu_data.linear_acceleration.x, imu_data.linear_acceleration.y, imu_data.linear_acceleration.z)


# try:
#     while not rospy.is_shutdown():
#         try:
#             (header, imu_data) = bag.read_messages(['/iris_0/imu_gazebo'])
#             print(imu_data.header.stamp ,imu_data.angular_velocity.x, imu_data.angular_velocity.y, imu_data.angular_velocity.z, imu_data.linear_acceleration.x, imu_data.linear_acceleration.y, imu_data.linear_acceleration.z)
#         except :
#             continue
# except KeyboardInterrupt:
#     pass
# finally:
#     bag.close()
