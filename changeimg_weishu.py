# coding=utf-8
import cv2
from HaveFun import common
import os

def readtime(ts_path):
    timestamps = []
    fin = open(ts_path, 'r')
    line = fin.readline().strip()
    while line:
        parts = line.split(",")
        ts = int(parts[0])
        # ts = "{:13}".format(parts[0])
        # ts = f"{parts[0]:13}"
        timestamps.append(ts)
        line = fin.readline().strip()
    return timestamps

params = []

params.append(["/media/hy/B0CC6321622802A9/ORB-Exp/XTDrone/Seq005/image_right", "/media/hy/B0CC6321622802A9/ORB-Exp/XTDrone/Seq005/image_right_new", ".png", ".png", "/media/hy/B0CC6321622802A9/ORB-Exp/XTDrone/Seq005/time.txt"])

for k in range(len(params)):
    source_dir = params[k][0]
    target_dir = params[k][1]

    source_type = params[k][2]
    target_type = params[k][3]

    ts_path = params[k][4]
    # print(type(ts_path))
    timestamps = []
    timestamps = readtime(ts_path)
    # print(timestamps[100])

    paths, names, files = common.findFiles(source_dir, source_type)
    common.isDirExist(target_dir)

    # # ts_path = source_dir[:source_dir.rfind(os.path.sep)]+"/timestamps.txt"
    # print(ts_path)
    # fout = open(ts_path, "w")

    for i in range(len(files)):
        tmp_img = cv2.imread(files[i])
        # bare_name = str("{:13}".format(timestamps[i]))
        bare_name = str(timestamps[i]).zfill(13)
        # bare_name = timestamps[i]
        print(bare_name)
        cv2.imwrite(target_dir+"/"+bare_name+target_type, tmp_img)
        # fout.write(bare_name+"\n")
        print(i+1, "/", len(files))

    # fout.close()