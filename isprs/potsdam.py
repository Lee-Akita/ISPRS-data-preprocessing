import os
import re
import tqdm
import cv2


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
            label = cv2.imread(os.path.join(self.Label_path, 'top_potsdam_' + flag + '_label.tif'))
            image = cv2.imread(os.path.join(self.RGB_path, 'top_potsdam_' + flag + '_RGB.tif'))
            dsm = cv2.imread(os.path.join(self.DSM_path, 'dsm_potsdam_' + flag + '.tif'), -1)
            # 由于标号6_7的标签有其他像素值，进行修正
            if flag == '6_7':
                label[label == 252] = 255
            # 将像素值进行对应的转换
            label[label == 255] = 1
            label = label[:, :, 2] * 4 + label[:, :, 1] * 2 + label[:, :, 0]
            label = label - 1
            label[label == 5] = 4
            label[label == 6] = 5
            # 开始进行切割
            min_x = min(image.shape[0], dsm.shape[0], label.shape[0])
            min_y = min(image.shape[1], dsm.shape[1], label.shape[1])
            range_x = min_x // split_size
            range_y = min_y // split_size
            for x in range(range_x):
                for y in range(range_y):
                    split_dsm = dsm[x * split_size:(x + 1) * split_size, y * split_size:(y + 1) * split_size]
                    split_image = image[x * split_size:(x + 1) * split_size, y * split_size:(y + 1) * split_size]
                    split_label = label[x * split_size:(x + 1) * split_size, y * split_size:(y + 1) * split_size]
                    cv2.imwrite(os.path.join(self.target_path, 'DSM', str(num) + '.tif'), split_dsm)
                    cv2.imwrite(os.path.join(self.target_path, 'RGB', str(num) + '.png'), split_image)
                    cv2.imwrite(os.path.join(self.target_path, 'Label', str(num) + '.png'), split_label)
                    num += 1
        tqdm_file_flag.close()
