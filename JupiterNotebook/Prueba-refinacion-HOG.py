#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:18:06 2020

@author: fher
"""

import numpy as np
import matplotlib.pyplot as plt

from skimage import filters
from skimage.data import camera
from skimage.util import compare_images
from skimage.io import imread, imshow
from skimage.color import rgb2gray, gray2rgb
from skimage.transform import resize
from skimage.feature import hog

dimx=160
dimy=90
nPixels=16
nCells=2
nOrients=8

imageOr = imread('/home/fher/Documentos/Curso CIBR/CIBR-Aves/gorrion/gorrion-real.jpg')
imgGray = rgb2gray(imageOr)
edge_roberts = filters.roberts(imgGray)
resized_img= resize(edge_roberts, (dimy,dimx)) 
#edge_sobel = filters.sobel(image)
#edge_sobel = resize(edge_sobel, (dimy,dimx)) 

fig, axes = plt.subplots(ncols=2, sharex=True, sharey=True,
                         figsize=(8, 4))

fd, hog_image = hog(gray2rgb(resized_img), orientations=nOrients, pixels_per_cell=(nPixels, nPixels), 
                    cells_per_block=(nCells, nCells), visualize=True, multichannel=True)

axes[0].imshow(resize(edge_roberts,(dimy,dimx)), cmap=plt.cm.gray)
axes[0].set_title('Roberts/Sobel Edge Detection')

axes[1].imshow(hog_image, cmap=plt.cm.gray)
axes[1].set_title('HOG Image')

for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()