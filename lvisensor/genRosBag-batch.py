# coding=utf-8
import sys
import os
from turtle import Turtle
import numpy as np
import cv2
import rosbag
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, Imu
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import PointField
from velodyne_msgs.msg import VelodyneScan
from velodyne_msgs.msg import VelodynePacket
from geometry_msgs.msg import Quaternion

def findFiles(root_dir, filter_type, reverse=False):
    """
    在指定目录查找指定类型文件 -> paths, names, files
    :param root_dir: 查找目录
    :param filter_type: 文件类型
    :param reverse: 是否返回倒序文件列表，默认为False
    :return: 路径、名称、文件全路径
    """

    separator = os.path.sep
    paths = []
    names = []
    files = []
    for parent, dirname, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(filter_type):
                paths.append(parent + separator)
                names.append(filename)
    for i in range(paths.__len__()):
        files.append(paths[i] + names[i])
    print(names.__len__().__str__() + " files have been found.")

    paths = np.array(paths)
    names = np.array(names)
    files = np.array(files)

    index = np.argsort(files)

    paths = paths[index]
    names = names[index]
    files = files[index]

    paths = list(paths)
    names = list(names)
    files = list(files)

    if reverse:
        paths.reverse()
        names.reverse()
        files.reverse()
    return paths, names, files


def readIMU(imu_path):
    timestamps = []
    q1s = []
    q2s = []
    q3s = []
    q0s = []
    wxs = []
    wys = []
    wzs = []
    axs = []
    ays = []
    azs = []
    fin = open(imu_path, 'r')
    fin.readline()
    line = fin.readline().strip()
    while line:
        parts = line.split(",")
        ts = float(parts[0]) / 10e8
        q1 = float(parts[1])
        q2 = float(parts[2])
        q3 = float(parts[3])
        q0 = float(parts[4])
        wx = float(parts[5])
        wy = float(parts[6])
        wz = float(parts[7])
        ax = float(parts[8])
        ay = float(parts[9])
        az = float(parts[10])
        timestamps.append(ts)

        q1s.append(q1)
        q2s.append(q2)
        q3s.append(q3)
        q0s.append(q0)
        wxs.append(wx)
        wys.append(wy)
        wzs.append(wz)
        axs.append(ax)
        ays.append(ay)
        azs.append(az)
        line = fin.readline().strip()

    return timestamps, q1s, q2s, q3s, q0s, wxs, wys, wzs, axs, ays, azs


def readLidarCSV(file_path):
    point_list = []
    fin = open(file_path, 'r')
    fin.readline()
    line = fin.readline().strip()
    while line:
        parts = line.split(",")
        intensity = float(parts[0])
        laser_id = float(parts[1])
        azimuth = float(parts[2])
        distance = float(parts[3])
        timestamp = float(parts[4])
        vertical_angle = float(parts[5])
        pos_x = float(parts[6])
        pos_y = float(parts[7])
        pos_z = float(parts[8])
        # timestamp = float(parts[9])

        point_list.append([pos_x, pos_y, pos_z, intensity, laser_id, timestamp, distance, azimuth, vertical_angle])

        line = fin.readline().strip()
    
    return point_list


if __name__ == '__main__':
    search_dir = sys.argv[1]
    bag_path = sys.argv[2]

    # # camera参数
    # img_dir = search_dir + "/Camera/0001"
    # img_type = ".jpg"
    # img_topic_name = "/image_raw"

    # imu参数
    imu_path = search_dir + "/Synchronise/IMU.csv"
    imu_topic_name = "/imu_raw"

    # lidar参数
    lidar_dir = search_dir + "/VLP16"
    lidar_type = ".csv"
    lidar_topic_name = "/velodyne_points"

    # 新建ROS Bag输出
    bag_out = rosbag.Bag(bag_path, 'w')

    # IMU数据转换
    # ----------------------------------------------------------
    imu_ts, q1s, q2s, q3s, q0s, wxs, wys, wzs, axs, ays, azs = readIMU(imu_path)
    imu_msg = Imu()
    q = Quaternion()
    angular_v = Vector3()
    linear_a = Vector3()

    for i in range(len(imu_ts)):
        imu_ts_ros = rospy.rostime.Time.from_sec(imu_ts[i])
        imu_msg.header.stamp = imu_ts_ros

        q.x = q1s[i]
        q.y = q2s[i]
        q.z = q3s[i]
        q.w = q0s[i]
        
        angular_v.x = wxs[i]
        angular_v.y = wys[i]
        angular_v.z = wzs[i]

        linear_a.x = axs[i]
        linear_a.y = ays[i]
        linear_a.z = azs[i]

        imu_msg.orientation = q
        imu_msg.angular_velocity = angular_v
        imu_msg.linear_acceleration = linear_a

        bag_out.write(imu_topic_name, imu_msg, imu_ts_ros)
        print('imu:', i, '/', len(imu_ts))
    # ----------------------------------------------------------

    # # Camera数据转换
    # # ----------------------------------------------------------
    # paths, names, files = findFiles(img_dir, img_type)
    # cb = CvBridge()

    # for i in range(len(files)):
    #     print('image:', i, '/', len(files))

    #     frame_img = cv2.imread(files[i])
    #     timestamp = int(names[i].split(".")[0]) / 10e8

    #     ros_ts = rospy.rostime.Time.from_sec(timestamp)
    #     ros_img = cb.cv2_to_imgmsg(frame_img, encoding='bgr8')
    #     ros_img.header.stamp = ros_ts
    #     bag_out.write(img_topic_name, ros_img, ros_ts)
    # # ----------------------------------------------------------

    # LiDAR数据转换
    # ----------------------------------------------------------
    paths, names, files = findFiles(lidar_dir, lidar_type)

    for i in range(len(files)):
        ts = float(names[i].split(".")[0]) / 1e9

        tmp_path = files[i]

        point_list = readLidarCSV(tmp_path)

        points = np.array(point_list)

        lidar_msg = PointCloud2()
        lidar_msg.header.frame_id = "map"
        lidar_ts_ros = rospy.rostime.Time.from_sec(ts)
        lidar_msg.header.stamp = lidar_ts_ros

        if len(points.shape) == 3:
            lidar_msg.height = points.shape[1]
            lidar_msg.width = points.shape[0]
        else:
            lidar_msg.height = 1
            lidar_msg.width = len(points)
# point_list.append([pos_x, pos_y, pos_z, intensity, laser_id, timestamp, distance, azimuth, vertical_angle])
        # lidar_msg.fields = [
        #     PointField('x', 0, PointField.FLOAT32, 1),
        #     PointField('y', 4, PointField.FLOAT32, 1),
        #     PointField('z', 8, PointField.FLOAT32, 1),
        #     PointField('intensity', 12, PointField.FLOAT32, 1),
	    #     PointField('ring', 16, PointField.FLOAT32, 1),
	    #     PointField('time', 20, PointField.FLOAT32, 1),
        #     PointField('distance', 24, PointField.FLOAT32, 1),
        #     PointField('azimuth', 28, PointField.FLOAT32, 1),
        #     PointField('vertical_angle', 32, PointField.FLOAT32, 1),
        # ]
        lidar_msg.fields = [
            PointField('x', 0, PointField.FLOAT32, 1),
            PointField('y', 4, PointField.FLOAT32, 1),
            PointField('z', 8, PointField.FLOAT32, 1),
            PointField('intensity', 12, PointField.FLOAT32, 1),
	        PointField('ring', 16, PointField.FLOAT32, 1),
	        PointField('time', 20, PointField.FLOAT32, 1),
        ]
        lidar_msg.is_bigendian = False
        # lidar_msg.point_step = 28

        lidar_msg.point_step = 24
        lidar_msg.row_step = lidar_msg.point_step * points.shape[0]
        # lidar_msg.is_dense = False
        
        lidar_msg.is_dense = True
        lidar_msg.data = np.asarray(points, np.float32).tostring()

        bag_out.write(lidar_topic_name, lidar_msg, lidar_ts_ros)

        print("lidar", i + 1, "/", len(files))
    # ----------------------------------------------------------

    bag_out.close()
