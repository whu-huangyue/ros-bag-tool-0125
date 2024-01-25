# coding=utf-8
import sys
import os
import numpy as np
import cv2
import rosbag
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, Imu
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import PointField


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
        wx = float(parts[1])
        wy = float(parts[2])
        wz = float(parts[3])
        ax = float(parts[4])
        ay = float(parts[5])
        az = float(parts[6])
        timestamps.append(ts)

        wxs.append(wx)
        wys.append(wy)
        wzs.append(wz)
        axs.append(ax)
        ays.append(ay)
        azs.append(az)
        line = fin.readline().strip()
    return timestamps, wxs, wys, wzs, axs, ays, azs


def readLidarCSV(file_path):
    point_list = []
    fin = open(file_path, 'r')
    fin.readline()
    line = fin.readline().strip()
    while line:
        parts = line.split(",")
        intensity = float(parts[0])
        azimuth = float(parts[2])
        distance = float(parts[3])
        vertical_angle = float(parts[5])
        pos_x = float(parts[6])
        pos_y = float(parts[7])
        pos_z = float(parts[8])

        point_list.append([pos_x, pos_y, pos_z, intensity, distance, azimuth, vertical_angle])

        line = fin.readline().strip()

    return point_list


if __name__ == '__main__':
    search_dir = sys.argv[1]
    bag_path = sys.argv[2]

    # camera参数
    img_dir = search_dir + "/Camera/0001"
    img_type = ".jpg"
    img_topic_name = "/image_raw"

    # 新建ROS Bag输出
    bag_out = rosbag.Bag(bag_path, 'w')

    # Camera数据转换
    # ----------------------------------------------------------
    paths, names, files = findFiles(img_dir, img_type)
    cb = CvBridge()

    for i in range(len(files)):
        print('image:', i, '/', len(files))

        frame_img = cv2.imread(files[i])
        timestamp = int(names[i].split(".")[0]) / 10e8

        ros_ts = rospy.rostime.Time.from_sec(timestamp)
        ros_img = cb.cv2_to_imgmsg(frame_img, encoding='bgr8')
        ros_img.header.stamp = ros_ts
        bag_out.write(img_topic_name, ros_img, ros_ts)
    # ----------------------------------------------------------

    bag_out.close()
