import os
import numpy as np
from PIL import Image
import matplotlib.pylab as plt

dataset_path = r'分割后的数据集'

# 测试接口
if __name__ == '__main__':
    a = np.array(Image.open(os.path.join(dataset_path, 'RGB', '20.png')))
    b = np.array(Image.open(os.path.join(dataset_path, 'Label', '20.png')))
    plt.subplot(1, 2, 1)
    plt.imshow(a)
    plt.subplot(1, 2, 2)
    plt.imshow(b)
    plt.show()
