import os
from skimage.io import imread #, imshow
from skimage.transform import resize
from skimage.feature import hog
#from skimage import exposure
#from scipy.spatial import distance
#from skimage.color import rgb2hsv
from skimage.color import rgb2gray, gray2rgb, rgb2hsv
from skimage import filters
import numpy as np

class Imagen:

    def __init__(self,nombre,vecHOG, vecColor):

        self.nombre = nombre
        self.vecHOG = vecHOG
        self.vecColor = vecColor

dimx=160
dimy=90
nPixels=16
nCells=2
nOrients=8

arrImagenes = []

contenido = os.listdir('/home/fher/Documentos/Curso CIBR/CIBR-Aves/gorrion')
for ruta_imagen in contenido:
    img = imread('gorrion/'+ruta_imagen)    
    
    #Aplicamos el filtro Edge Roberts para quitar un poco las texturas de las ramas    
    imgGray = rgb2gray(img)
    edge_roberts = filters.roberts(imgGray)
    #Se reconfigura el tamaño para tener un vector de la misma dimension para todas las imagenes
    resized_img = resize(edge_roberts, (dimy,dimx))
    # Extracción de la caracteristica HOG
    fd, hog_image = hog(gray2rgb(resized_img), orientations=nOrients, pixels_per_cell=(nPixels, nPixels), 
                    cells_per_block=(nCells, nCells), visualize=True, multichannel=True)
    
    #Descomposición de planos RGB
    planoR = img[:,:,0]
    planoG = img[:,:,1]
    planoB = img[:,:,2]
    
    #Valores medios de los planos
    meanR = np.mean(img[:,:,0])
    meanG = np.mean(img[:,:,1])
    meanB = np.mean(img[:,:,2])
    
    #Extracción de caracteristivas HSV
    img_hsv = rgb2hsv(img)
    meanH = np.mean(img_hsv[:,:,0])
    meanS = np.mean(img_hsv[:,:,1])
    meanV = np.mean(img_hsv[:,:,2])
    
    #Creación del vector de caracteristicas de color
    fColor = [meanR, meanG, meanB, meanH, meanS, meanV]
    
    #Normalizacion del vector 
    fNormColor = fColor / np.linalg.norm(fColor)
    
    
    #Creación del objeto imagen para guardar el nombre y los vectores de caracteristicas
    imagen_actual = Imagen(ruta_imagen,fd, fNormColor)
    #Se agrega al arreglo de caracteristicas de cada imagen
    arrImagenes.append(imagen_actual)    
    
