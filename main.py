from isprs.vaihingen import Vaihingen
from isprs.potsdam import Potsdam

if __name__ == '__main__':
    v = Vaihingen(dataset_path=r'数据集源路径',
                  target_path=r'目标路径')
    v.start_dealWith(split_size='分割的尺寸大小')
