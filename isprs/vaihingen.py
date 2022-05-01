import os
import cv2
import tqdm


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
            image = cv2.imread(os.path.join(self.RGB_path, file))
            dsm = cv2.imread(os.path.join(self.DSM_path, file), -1)
            label = cv2.imread(os.path.join(self.Label_path, file))
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
                    cv2.imwrite(os.path.join(self.target_path, 'DSM', str(num) + '.tiff'), split_dsm)
                    cv2.imwrite(os.path.join(self.target_path, 'RGB', str(num) + '.png'), split_image)
                    cv2.imwrite(os.path.join(self.target_path, 'Label', str(num) + '.png'), split_label)
                    num += 1
        tqdm_flag.close()
