from isprs.vaihingen import Vaihingen

if __name__ == '__main__':
    v = Vaihingen(dataset_path=r'ISPRS源路径', target_path=r'处理完数据保存的路径')
    v.start_dealWith(split_size='分割后单张图片的尺寸')
