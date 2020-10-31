# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:00:24 2020

@author: Packo
"""
import os
from skimage.io import imread #, imshow
from skimage.transform import resize
from skimage.feature import hog
from skimage.color import rgb2gray, gray2rgb, rgb2hsv
from skimage import filters
from Imagen import Imagen
from datos import guardarVecImagenes, leerDatos
import numpy as np
from skimage.io import imread #, imshow
from scipy.spatial import distance

dimx=160
dimy=90
nPixels=16
nCells=2
nOrients=8

def caracteristicasImage(img):
        imgGray = rgb2gray(img)
        edge_roberts = filters.roberts(imgGray)
        #Se reconfigura el tamaño para tener un vector de la misma dimension para todas las imagenes
        resized_img = resize(edge_roberts, (dimy,dimx))
        # Extracción de la caracteristica HOG
        fd, hog_image = hog(gray2rgb(resized_img), orientations=nOrients, pixels_per_cell=(nPixels, nPixels), 
                        cells_per_block=(nCells, nCells), visualize=True, multichannel=True)
                
        
        #Valores medios de los planos RGB
        meanR = np.mean(img[:,:,0]) # Plano R
        meanG = np.mean(img[:,:,1]) # Plano G
        meanB = np.mean(img[:,:,2]) # Plano B
        
        #Extracción de caracteristivas HSV
        img_hsv = rgb2hsv(img)
        meanH = np.mean(img_hsv[:,:,0]) #Plano H
        meanS = np.mean(img_hsv[:,:,1]) #Plano S
        meanV = np.mean(img_hsv[:,:,2]) #Plano V
        
        #Creación de los vectores de caracteristicas de color
        fColorRGB = [meanR, meanG, meanB]
        fColorHSV = [meanH, meanS, meanV]
        
        #Normalizacion de los vectores de color
        fNormRGB = fColorRGB / np.linalg.norm(fColorRGB)
        fNormHSV = fColorHSV / np.linalg.norm(fColorHSV)
        
        
        #Creación del objeto imagen para guardar el nombre y los vectores de caracteristicas
        imagen_actual = Imagen("gorrion",fd, fNormRGB, fNormHSV)
        return imagen_actual
        
def mayorSimilitud(image_actual):
    datos = leerDatos()

    hog = distance.minkowski(image_actual.vecHOG, datos[0]["vecHOG"],2)
    rgb = distance.minkowski(image_actual.vecRGB, datos[0]["vectorRGB"],2)
    hsv = distance.minkowski(image_actual.vecHSV, datos[0]["vecHSV"],2)
    datoActual = [datos[0]["nombreImg"], rgb, hsv, hog]
    distanciaActual = hog + rgb + hsv
    cont = 0
    
    for i in datos:
        if(cont != 0):
            hog = distance.minkowski(image_actual.vecHOG, i["vecHOG"],2)
            rgb = distance.minkowski(image_actual.vecRGB, i["vectorRGB"],2)
            hsv = distance.minkowski(image_actual.vecHSV, i["vecHSV"],2)            
            distancia = hog + rgb + hsv            
            dato = [i["nombreImg"], rgb, hsv, hog]
            if(distanciaActual > distancia):
                distanciaActual = distancia
                datoActual = dato            
        else:
             cont = 1
         
    
    print("La imagen se parece a: " + datoActual[0])

img = imread('tucan.jpg')
image_actual = caracteristicasImage(img)
mayorSimilitud(image_actual)