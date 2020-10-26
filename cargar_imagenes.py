import os
from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
from scipy.spatial import distance
from skimage.color import rgb2hsv

class Imagen:

    def __init__(self,nombre,vecHOG):

        self.nombre = nombre
        self.vecHOG = vecHOG

dimx=160
dimy=90
nPixels=16
nCells=2
nOrients=8

arrImagenes = []

contenido = os.listdir('/home/fher/Documentos/Curso CIBR/CIBR-Aves/gorrion')
for ruta_imagen in contenido:
    img = imread('gorrion/'+ruta_imagen)    
    resized_img = resize(img, (dimy,dimx))
    # Extracción de la caracteristica HOG
    fd, hog_image = hog(resized_img, orientations=nOrients, pixels_per_cell=(nPixels, nPixels), 
                    cells_per_block=(nCells, nCells), visualize=True, multichannel=True)
    #Creación del objeto imagen para guardar el nombre y los vectores de caracteristicas
    imagen_actual = Imagen(ruta_imagen,fd)
    
    arrImagenes.append(imagen_actual)    
    
