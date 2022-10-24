import os
import re
import numpy as np
import tqdm
from PIL import Image

Potsdam_COLOR_MAP = [
    [255, 255, 255],  # 不透水路面 Impervious surfaces (RGB: 255, 255, 255)
    [0, 0, 255],  # 建筑物 Building (RGB: 0, 0, 255)
    [0, 255, 255],  # 低植被 Low vegetation (RGB: 0, 255, 255)
    [0, 255, 0],  # 树木 Tree (RGB: 0, 255, 0)
    [255, 255, 0],  # 汽车 Car (RGB: 255, 255, 0)
    [255, 0, 0]  # 背景 Clutter/background (RGB: 255, 0, 0)
]


def RGB2Label(label, COLOR_MAP):
    width, height = label.shape[0], label.shape[1]
    temp_mask = np.zeros(shape=(width, height))
    for index, color in enumerate(COLOR_MAP):
        locations = np.all(label == color, axis=-1)
        temp_mask[locations] = index
    return temp_mask.astype(dtype=np.int8)


class Potsdam:
    def __init__(self, dataset_path, target_path):
        my_re = re.compile(r'\d+_\d+')
        self.dataset_path = dataset_path
        self.target_path = target_path
        self.DSM_path = os.path.join(dataset_path, 'DSM')
        self.RGB_path = os.path.join(dataset_path, 'RGB')
        self.Label_path = os.path.join(dataset_path, 'Label')
        self.file_flag = [my_re.findall(name)[-1] for name in os.listdir(self.DSM_path)]

    def start_dealWith(self, split_size):
        num = 0
        tqdm_file_flag = tqdm.tqdm(self.file_flag, total=len(self.file_flag))
        for flag in tqdm_file_flag:
            # 进行数据的读取
            label = np.array(Image.open(os.path.join(self.Label_path, 'top_potsdam_' + flag + '_label.tif')))
            image = np.array(Image.open(os.path.join(self.RGB_path, 'top_potsdam_' + flag + '_RGB.tif')))
            dsm = np.array(Image.open(os.path.join(self.DSM_path, 'dsm_potsdam_' + flag + '.tif')))
            # 由于标号6_7的标签有其他像素值，进行修正
            if flag == '6_7':
                label[label == 252] = 255
            # 将像素值进行对应的转换
            mask = RGB2Label(label=label, COLOR_MAP=Potsdam_COLOR_MAP)
            # 开始进行切割
            min_x = min(image.shape[0], dsm.shape[0], mask.shape[0])
            min_y = min(image.shape[1], dsm.shape[1], mask.shape[1])
            range_x = min_x // split_size
            range_y = min_y // split_size
            for x in range(range_x):
                for y in range(range_y):
                    split_dsm = dsm[x * split_size:(x + 1) * split_size, y * split_size:(y + 1) * split_size]
                    split_image = image[x * split_size:(x + 1) * split_size, y * split_size:(y + 1) * split_size]
                    split_mask = mask[x * split_size:(x + 1) * split_size, y * split_size:(y + 1) * split_size]
                    Image.fromarray(split_dsm).save(os.path.join(self.target_path, 'DSM', str(num) + '.tif'))
                    Image.fromarray(split_image).save(os.path.join(self.target_path, 'RGB', str(num) + '.png'))
                    Image.fromarray(split_mask).save(os.path.join(self.target_path, 'Label', str(num) + '.png'))
                    num += 1
        tqdm_file_flag.close()
