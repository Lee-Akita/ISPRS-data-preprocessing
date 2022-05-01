import glob
import tqdm
import cv2
import numpy as np

haha = glob.glob('/Users/leeakita/Desktop/Dataset/Label/*.png')
file_tqdm = tqdm.tqdm(haha, total=len(haha))
ge = set()
for i in file_tqdm:
    img = cv2.imread(i)
    for k in np.unique(img):
        ge.add(k)
file_tqdm.close()
print(ge)
