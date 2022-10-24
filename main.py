from isprs.vaihingen import Vaihingen
from isprs.potsdam import Potsdam

if __name__ == '__main__':
    v = Vaihingen(dataset_path=r'C:\Users\akitalee\Desktop\Vaihingen',
                  target_path=r'C:\Users\akitalee\Desktop\VaihingenDataset\train')
    v.start_dealWith(split_size=256)
