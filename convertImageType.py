# coding=utf-8
import cv2
from HaveFun import common
import os

params = []

params.append(["/home/hy/下载/FLSea/canyon2/canyon2/imgs/LFT", "/home/hy/下载/FLSea/canyon2/canyon2/imgs/LFT2", ".tif", ".jpg"])
params.append(["/home/hy/下载/FLSea/canyon2/canyon2/imgs/RGT", "/home/hy/下载/FLSea/canyon2/canyon2/imgs/RGT2", ".tif", ".jpg"])

params.append(["/home/hy/下载/FLSea/rock_garden1/rock_garden1/imgs/LFT", "/home/hy/下载/FLSea/rock_garden1/rock_garden1/imgs/LFT2", ".tif", ".jpg"])
params.append(["/home/hy/下载/FLSea/rock_garden1/rock_garden1/imgs/RGT", "/home/hy/下载/FLSea/rock_garden1/rock_garden1/imgs/RGT2", ".tif", ".jpg"])

params.append(["/home/hy/下载/FLSea/rock_garden2/rock_garden2/imgs/LFT", "/home/hy/下载/FLSea/rock_garden2/rock_garden2/imgs/LFT2", ".tif", ".jpg"])
params.append(["/home/hy/下载/FLSea/rock_garden2/rock_garden2/imgs/RGT", "/home/hy/下载/FLSea/rock_garden2/rock_garden2/imgs/RGT2", ".tif", ".jpg"])


for k in range(len(params)):
    source_dir = params[k][0]
    target_dir = params[k][1]

    source_type = params[k][2]
    target_type = params[k][3]

    paths, names, files = common.findFiles(source_dir, source_type)
    common.isDirExist(target_dir)

    ts_path = source_dir[:source_dir.rfind(os.path.sep)]+"/timestamps.txt"
    print(ts_path)
    fout = open(ts_path, "w")

    for i in range(len(files)):
        tmp_img = cv2.imread(files[i])
        bare_name = names[i][:-4][-6:]
        cv2.imwrite(target_dir+"/"+bare_name+target_type, tmp_img)
        fout.write(bare_name+"\n")
        print(i+1, "/", len(files))

    fout.close()