import cv2
import numpy as np
import os

def tif_to_png(image_path,save_path):
    """
    :param image_path: *.tif image path
    :param save_path: *.png image path
    :return:
    """
    # print(image_path)
    img = cv2.imread(image_path,3)
    # print(img)
    # print(img.dtype)
    filename = image_path.split('/')[-1].split('.')[0]
    print(filename)
    save_path = save_path + '/' + filename + '.png'
    cv2.imwrite(save_path,img)

if __name__ == '__main__':
    root_path = '/media/hy/Xuhui-Database/Datasets/SLAM/NCLT/2012-05-26_lb3/2012-05-26/lb3/Cam2/'
    save_path = '/media/hy/B0CC6321622802A9/NCLT/Cam2_2/'
    # print(root_path)
    image_files = os.listdir(root_path)
    for image_file in image_files:
        tif_to_png(root_path + image_file,save_path)