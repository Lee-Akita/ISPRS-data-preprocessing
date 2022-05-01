import os
import re
import cv2
import numpy as np

data_path = r'C:\Users\akitalee\Desktop\Potsdam'
my_re = re.compile(r'\d+')

my = os.listdir(os.path.join(data_path, 'Label'))
for i in my:
    img = cv2.imread(os.path.join(data_path, 'Label', i))
    print(np.unique(img), end='   ')
    print(i)
