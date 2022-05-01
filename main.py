from isprs.potsdam import Potsdam

if __name__ == '__main__':
    po = Potsdam(dataset_path=r'/Users/leeakita/Desktop/Potsdam', target_path=r'/Users/leeakita/Desktop/Dataset')
    po.start_dealWith(split_size=512)
