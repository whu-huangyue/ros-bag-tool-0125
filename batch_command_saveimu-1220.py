#coding=utf-8
import os
commands = []
commands.append("""python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py  /media/hy/Xuhui-Database1/Datasets/SLAM/FusionPortable/20220215_canteen_night.bag /stereo/davis_right/imu/data_raw /media/hy/B0CC6321622802A9/ORB-Exp/FP/20220215_canteen_night/imu.csv""")
commands.append("""python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py  /media/hy/Xuhui-Database1/Datasets/SLAM/FusionPortable/20220215_garden_night.bag /stereo/davis_right/imu/data_raw /media/hy/B0CC6321622802A9/ORB-Exp/FP/20220215_garden_night/imu.csv""")
commands.append("""python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py  /media/hy/Xuhui-Database1/Datasets/SLAM/FusionPortable/20220216_corridor_day.bag /stereo/davis_right/imu/data_raw /media/hy/B0CC6321622802A9/ORB-Exp/FP/20220216_corridor_day/imu.csv""")
commands.append("""python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py  /media/hy/Xuhui-Database1/Datasets/SLAM/FusionPortable/20220216_escalator_day.bag /stereo/davis_right/imu/data_raw /media/hy/B0CC6321622802A9/ORB-Exp/FP/20220216_escalator_day/imu.csv""")
commands.append("""python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py  /media/hy/Xuhui-Database1/Datasets/SLAM/FusionPortable/20220216_MCR_fast.bag /stereo/davis_right/imu/data_raw /media/hy/B0CC6321622802A9/ORB-Exp/FP/20220216_MCR_fast/imu.csv""")
commands.append("""python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py  /media/hy/Xuhui-Database1/Datasets/SLAM/FusionPortable/20220226_campus_road_day.bag /stereo/davis_right/imu/data_raw /media/hy/B0CC6321622802A9/ORB-Exp/FP/20220226_campus_road_day/imu.csv""")


# command1 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/XTDrone/Seq001/2023-11-28-11-16-29.bag /iris_0/imu_gazebo"""
# command2 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/XTDrone/Seq002/2023-11-28-11-25-21.bag /iris_0/imu_gazebo"""
# command3 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/XTDrone/Seq003/2023-11-28-11-36-31.bag /iris_0/imu_gazebo"""
# command4 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/XTDrone/Seq004/2023-11-28-11-50-35.bag /iris_0/imu_gazebo"""

# command5 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/MVSEC/outdoor_day/outdoor_day1_data.bag /visensor/imu"""

# command6 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/NCD/1036/rooster_2020-03-10-10-36-30_0.bag /camera/imu"""
# command7 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/NCD/1050/rooster_2020-03-10-10-50-26_5.bag /camera/imu"""

# command8 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/NTU-Viral/eee_01/eee_01.bag /imu/imu"""
# command9 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/NTU-Viral/eee_02/eee_02.bag /imu/imu"""
# command10 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/NTU-Viral/eee_03/eee_03.bag /imu/imu"""
# command11 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/NTU-Viral/nya_02/nya_02.bag /imu/imu"""
# command12 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/NTU-Viral/nya_03/nya_03.bag /imu/imu"""
# command13 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/NTU-Viral/sbs_01/sbs_01.bag /imu/imu"""
# command14 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/NTU-Viral/sbs_02/sbs_02.bag /imu/imu"""
# command15 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/NTU-Viral/sbs_03/sbs_03.bag /imu/imu"""

# command16 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/VID/indoor_loadless_8_3096.1g_109.17s/indoor_loadless_8_3096.1g_109.17s.bag /djiros/imu"""
# command17 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/VID/indoor_loadless_hovor_3096.1g_79.04s/indoor_loadless_hovor_3096.1g_79.04s.bag /djiros/imu"""

# command18 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/WHU/record/2023-12-14-15-55-48/2023-12-14-15-55-48.bag /camera/imu"""
# command19 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/ORB-Exp/WHU/record/2023-12-14-16-04-30/2023-12-14-16-04-30.bag /camera/imu"""

# command20 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/scene003-1202/join.bag /imu"""
# command21 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/scene006-1202/join.bag /imu"""
# command22 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/scene009-1202/join.bag /imu"""
# command23 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/scene052-1202/join.bag /imu"""
# command24 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/scene076-1202/join.bag /imu"""
# command25 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/scene100-1202/join.bag /imu"""
# command26 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/scene106-1202/join.bag /imu"""
# command27 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/scene115-1202/join.bag /imu"""
# command28 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/scene135-1205/join.bag /imu"""
# command29 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/scene137-1202/join.bag /imu"""
# command30 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/scene163-1202/join.bag /imu"""
# command31 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/scene174-1202/join.bag /imu"""
# command32 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/scene175-1202/join.bag /imu"""
# command33 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene007/join.bag /imu"""
# command34 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene048/join.bag /imu"""
# command35 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene055/join.bag /imu"""
# command36 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene075/join.bag /imu"""
# command37 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene080/join.bag /imu"""
# command38 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene092/join.bag /imu"""
# command39 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene103/join.bag /imu"""
# command40 = """python2 /home/hy/ROS-Bag-Tools/saveimufrombag.py /media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene165/join.bag /imu"""


# commands.append(command1)
# commands.append(command2)
# commands.append(command3)
# commands.append(command4)
# commands.append(command5)
# commands.append(command6)
# commands.append(command7)
# commands.append(command8)
# commands.append(command9)
# commands.append(command10)
# commands.append(command11)
# commands.append(command12)
# commands.append(command13)
# commands.append(command14)
# commands.append(command15)
# commands.append(command16)
# commands.append(command17)
# commands.append(command18)
# commands.append(command19)
# commands.append(command20)
# commands.append(command21)
# commands.append(command22)
# commands.append(command23)
# commands.append(command24)
# commands.append(command25)
# commands.append(command26)
# commands.append(command27)
# commands.append(command28)
# commands.append(command29)
# commands.append(command30)
# commands.append(command31)
# commands.append(command32)
# commands.append(command33)
# commands.append(command34)
# commands.append(command35)
# commands.append(command36)
# commands.append(command37)
# commands.append(command38)
# commands.append(command39)
# commands.append(command40)

for i in range(len(commands)):
    cur_command = commands[i]
    print(i+1, "/", len(commands))
    print(cur_command)
    os.system(cur_command)