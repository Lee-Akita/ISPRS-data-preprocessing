import os
import re


class Potsdam:
    def __init__(self, dataset_path, target_path):
        self.my_re = re.compile(r'\d+_\d+')
        self.dataset_path = dataset_path
        self.target_path = target_path
        self.DSM_path = os.path.join(dataset_path, 'DSM')
        self.RGB_path = os.path.join(dataset_path, 'RGB')
        self.Label_path = os.path.join(dataset_path, 'Label')
        self.file_flag = [self.my_re.findall(name)[-1] for name in os.listdir(self.DSM_path)]

    def start_dealWith(self):
        print(self.file_flag)


if __name__ == '__main__':
    po = Potsdam(dataset_path=r'/Users/leeakita/Desktop/Potsdam', target_path=r'/Users/leeakita/Desktop/Dataset')
    po.start_dealWith()
