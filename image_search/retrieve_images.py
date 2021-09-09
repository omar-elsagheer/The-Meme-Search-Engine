import os
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np


def get_images(fe, img):
    features = []
    img_paths = []
    for feature_path in os.listdir(r"C:\\Users\\Omar\\Desktop\\CMPS 391\\Project\\Data\\images1.npy"):
        features.append(np.load("C:\\Users\\Omar\\Desktop\\CMPS 391\\Project\\Data\\images1.npy\\" + feature_path))
        img_paths.append(feature_path[:-3])
    features = np.array(features)
    # Extract its features
    image = Image.open("C:\\Users\\Omar\\Desktop\\CMPS 391\\Project\\Code\\web_interface\\static\\Queries\\" + img)
    query = fe.extract(image)
    # Calculate the similarity (distance) between images
    dists = np.linalg.norm(features - query, axis=1)
    # Extract 30 images that have lowest distance
    ids = np.argsort(dists)
    # scores = [(dists[ID], img_paths[ID]) for ID in ids]
    scores = [img_paths[ID] for ID in ids]
    return scores

# Visualize the result
# axes = []
# fig = plt.figure(figsize=(50, 50))
# for a in range(10):
#     score = scores[a]
#     axes.append(fig.add_subplot(5, 5, a + 1))
#     # subplot_title = str(score[0])
#     # axes[-1].set_title(subplot_title)
#     plt.axis('off')
#     plt.imshow(Image.open(score[1]))
# fig.tight_layout()
# plt.show()
