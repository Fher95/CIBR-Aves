#!/usr/bin/env python
# coding: utf-8

# In[1]:



#importing required libraries
from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
from scipy.spatial import distance
from skimage.color import rgb2hsv
import almacenarDatos
#get_ipython().run_line_magic('matplotlib', 'inline')

dimx=160
dimy=90
nPixels=16
nCells=2
nOrients=8
img = imread('gorrion/gorrion3.jpg')
imshow(img)


# In[2]:


#resizing image 
resized_img = resize(img, (dimy,dimx)) 

#Revertir imagen
resized_img=resized_img[:,::-1,:]
imshow(resized_img)         
print(resized_img.shape)


# In[3]:


fd, hog_image = hog(resized_img, orientations=nOrients, pixels_per_cell=(nPixels, nPixels), 
                    cells_per_block=(nCells, nCells), visualize=True, multichannel=True)
len(fd)


# In[4]:


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), sharex=True, sharey=True) 

ax1.imshow(resized_img, cmap=plt.cm.gray) 
ax1.set_title('Input image') 

# Rescale histogram for better display 
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10)) 

ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray) 
ax2.set_title('Histogram of Oriented Gradients')

plt.show()


# In[5]:


img2 = imread('gorrion/gorrion-real.jpg')
imshow(img2)


# In[17]:


resized_img2 = resize(img2, (dimy,dimx)) 
#Convertir a hsv
#hsv_img = rgb2hsv(resized_img2)
#imshow(hsv_img)  
imshow(resized_img2) 
print(resized_img2.shape)


# In[7]:


fd2, hog_image2 = hog(resized_img2, orientations=nOrients, pixels_per_cell=(nPixels, nPixels), 
                    cells_per_block=(nCells, nCells), visualize=True, multichannel=True)
len(fd2)


# In[8]:


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), sharex=True, sharey=True) 

ax1.imshow(resized_img2, cmap=plt.cm.gray) 
ax1.set_title('Input image') 

# Rescale histogram for better display 
hog_image_rescaled2 = exposure.rescale_intensity(hog_image2, in_range=(0, 10)) 

ax2.imshow(hog_image_rescaled2, cmap=plt.cm.gray) 
ax2.set_title('Histogram of Oriented Gradients')

plt.show()


# In[9]:


img3 = imread('perro.jpg')
imshow(img3)


# In[10]:


resized_img3 = resize(img3, (dimy,dimx)) 
#hsv_img = rgb2hsv(resized_img3)
#imshow(hsv_img)
imshow(resized_img3) 
print(resized_img3.shape)


# In[11]:


fd3, hog_image3 = hog(resized_img3, orientations=nOrients, pixels_per_cell=(nPixels, nPixels), 
                    cells_per_block=(nCells, nCells), visualize=True, multichannel=True)
len(fd3)


# In[12]:



fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), sharex=True, sharey=True) 

ax1.imshow(resized_img3, cmap=plt.cm.gray) 
ax1.set_title('Input image') 

# Rescale histogram for better display 
hog_image_rescaled3 = exposure.rescale_intensity(hog_image3, in_range=(0, 10)) 

ax2.imshow(hog_image_rescaled3, cmap=plt.cm.gray) 
ax2.set_title('Histogram of Oriented Gradients')

plt.show()


# In[13]:


distance.minkowski(fd, fd2, 2)


# In[14]:


distance.minkowski(fd, fd3, 2)


# In[15]:


distance.minkowski(fd2, fd3, 2)


# In[ ]:

almacenarDatos.guardar(fd)



