import cv2
import sys
import os
import numpy as np

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

if __name__ == '__main__':
    img_path = sys.argv[1]

    paths, names, files = findFiles(img_path, '.png')

    # print(files[0])

    for i in range(len(files)):
        print('image:',i,'/',len(files))
        trans_img = cv2.transpose(cv2.imread(files[i]))
        new_img = cv2.flip(trans_img,1)
        cv2.imwrite(files[i], new_img)
    # cv2.imshow('clock90', new_img)
    # cv2.waitKey(0)