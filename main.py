from isprs.potsdam import Potsdam

if __name__ == '__main__':
    po = Potsdam(dataset_path=r'C:\Users\akitalee\Desktop\Potsdam', target_path=r'C:\Users\akitalee\Desktop\my')
    po.start_dealWith(split_size=512)
