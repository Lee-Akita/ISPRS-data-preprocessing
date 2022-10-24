from isprs.vaihingen import Vaihingen
from isprs.potsdam import Potsdam

if __name__ == '__main__':
    v = Potsdam(dataset_path=r'C:\Users\akitalee\Desktop\test1', target_path=r'C:\Users\akitalee\Desktop\hah')
    v.start_dealWith(split_size=256)
