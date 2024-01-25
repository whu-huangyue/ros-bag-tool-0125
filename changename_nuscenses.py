from asyncore import read
from hashlib import new
from operator import ne
import os
import sys
from time import time

def readtimestamp(timestamppath):
    timestamps = []
    fin = open(timestamppath, 'r')
    fin.readline()
    line = fin.readline().strip()
    # line = fin.readline
    while line:
        # parts = line.split(",")
        # ts = float(parts[0])/1e9
        ts = (line)
        # wx = float(parts[1])
        # wy = float(parts[2])
        # wz = float(parts[3])
        # ax = float(parts[4])
        # ay = float(parts[5])
        # az = float(parts[6])
        timestamps.append(ts)

        # wxs.append(wx)
        # wys.append(wy)
        # wzs.append(wz)
        # axs.append(ax)
        # ays.append(ay)
        # azs.append(az)
        line = fin.readline().strip()
    return timestamps

if __name__ == "__main__":
    timestamp1_path = sys.argv[1]

    timestamp2_path = sys.argv[2]

    # print(timestamp1_path)
    path = os.path.dirname(timestamp1_path)
    print(path)

    timestamp1 = readtimestamp(timestamp1_path)
    timestamp2 = readtimestamp(timestamp2_path)

    temp = path + '/' + timestamp1[0] + '.png'
    print(temp)
    for i in range(len(timestamp1)):
        # print(timestamp1[i])
        oldpath = path + '/' + timestamp1[i] + '.png'
        newpath = path + '/' + timestamp2[i] + '.png'
        os.rename(oldpath, newpath)
        # print(oldpath, newpath)
