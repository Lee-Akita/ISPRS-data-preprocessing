import os
import re
import cv2
import numpy as np
from PIL import Image
import matplotlib.pylab as plt

dataset_path = r'C:\Users\akitalee\Desktop\Vaihingen'

# 测试接口
if __name__ == '__main__':
    myre = re.compile('\d+')
    rgb_path = os.listdir(os.path.join(dataset_path, 'RGB'))
    dsm_path = os.listdir(os.path.join(dataset_path, 'DSM'))
    label_path = os.listdir(os.path.join(dataset_path, 'Label'))
    print(label_path)
    print(dsm_path)
    print(rgb_path)
