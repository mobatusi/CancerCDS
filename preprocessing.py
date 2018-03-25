#!/anaconda/envs/py36
import numpy as np
import os
import cv2
from matplotlib import pyplot as plt

# View version number
print(cv2.__version__)

class imageupload():
    def __init__(self):
        self.imagepath = '/Users/mosadoluwaobatusin/Documents/Projects/CancerCDS/Data/dataset1/Module1.2_FeatureExtractionSelection_Data/Necrosis_1.png'

    # Load Image As Greyscale
    def grayscale(self):
    # Load image as grayscale
        image = cv2.imread(self.imagepath, cv2.IMREAD_GRAYSCALE)

        # Show image
        plt.imshow(image, cmap='gray'), plt.axis("off")
        plt.show()

    # Load Image As RGB
    def rgb(self):
        # Load image in color
        image_bgr = cv2.imread(self.imagepath, cv2.IMREAD_COLOR)

        # Convert to RGB
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

        # Show image
        plt.imshow(image_rgb), plt.axis("off")
        plt.show()

img = imageupload()
img.grayscale()