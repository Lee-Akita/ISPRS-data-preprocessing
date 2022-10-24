import os
import re
import cv2
import numpy as np
from PIL import Image
import matplotlib.pylab as plt

rgb_path = r"C:\Users\akitalee\Desktop\hah\RGB\120.png"
label_path = r"C:\Users\akitalee\Desktop\hah\Label\120.png"

# 测试接口
if __name__ == '__main__':
    rgb = np.array(Image.open(rgb_path))
    label = np.array(Image.open(label_path))
    plt.subplot(1, 2, 1)
    plt.imshow(rgb)
    plt.subplot(1, 2, 2)
    plt.imshow(label)
    plt.show()
