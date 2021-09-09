import os

from PIL import Image
from feature_extractor import FeatureExtractor
from pathlib import Path
import numpy as np


fe = FeatureExtractor()
# Iterate through images (Change the path based on your image location)
for img_path in os.listdir(r'C:\\Users\\Omar\\Desktop\\CMPS 391\\Project\\Data\\images'):
    print(img_path)
    # Extract Features
    feature = fe.extract(img=Image.open('C:\\Users\\Omar\\Desktop\\CMPS 391\\Project\\Data\\images\\'+img_path))
    # Save the Numpy array (.npy) on designated path
    feature_path = "C:\\Users\\Omar\\Desktop\\CMPS 391\\Project\\Data\\images.npy\\"+img_path+".npy"
    np.save(feature_path, feature)
