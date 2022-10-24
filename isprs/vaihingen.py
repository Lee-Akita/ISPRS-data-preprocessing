import os
import tqdm
import numpy as np
from PIL import Image

Vaihingen_COLOR_MAP = [
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


class Vaihingen:
    def __init__(self, dataset_path, target_path):
        self.dataset_path = dataset_path
        self.target_path = target_path
        self.DSM_path = os.path.join(dataset_path, 'DSM')
        self.RGB_path = os.path.join(dataset_path, 'RGB')
        self.Label_path = os.path.join(dataset_path, 'Label')
        self.file_flag = os.listdir(self.Label_path)

    def start_dealWith(self, split_size):
        num = 0
        tqdm_flag = tqdm.tqdm(self.file_flag, total=len(self.file_flag))
        for file in tqdm_flag:
            # 进行数据的读取
            image = np.array(Image.open(os.path.join(self.RGB_path, file)))
            dsm = np.array(Image.open(os.path.join(self.DSM_path, file)))
            label = np.array(Image.open(os.path.join(self.Label_path, file)))
            # 将像素值进行对应的转换
            mask = RGB2Label(label=label, COLOR_MAP=Vaihingen_COLOR_MAP)
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
        tqdm_flag.close()
