import os
from skimage.io import imread #, imshow
from skimage.transform import resize
from skimage.feature import hog
#from skimage import exposure
#from scipy.spatial import distance
#from skimage.color import rgb2hsv
from skimage.color import rgb2gray, gray2rgb, rgb2hsv
from skimage import filters
from Imagen import Imagen
from datos import guardarVecImagenes
import numpy as np


        
dimx=160
dimy=90
nPixels=16
nCells=2
nOrients=8
imagenPrueba = None

ruta_base = 'Imagenes/'

def obtenerDirectorios(ruta):
    arrDirectorios = []    
    content = os.listdir(ruta)
    for fichero in content:
        if os.path.isdir(os.path.join(ruta,fichero)) and not fichero.endswith('.git'):
            arrDirectorios.append(fichero)
    return arrDirectorios

def obtenerSoloImagenes(ruta):
    vecImagenes = []
    contenido = os.listdir(ruta)
    for fichero in contenido:
        if os.path.isfile(os.path.join(ruta, fichero)) and (fichero.endswith('.jpg') or fichero.endswith('.jpeg')):
            vecImagenes.append(fichero)
    return vecImagenes

def recorrerDirectorios(vecDirectorios):
    print('Inicia procesamiento de imagenes...')
    for directorio in vecDirectorios:        
        print('Extrayendo caracteristicas de',directorio,'...')
        vecImgs = generarCaracteristicasDir(directorio)
        guardarVecImagenes(vecImgs,directorio)
        print(directorio,'finalizado.')        
    print('Se proceesaron todas las imagenes.')
        
def generarCaracteristicasDir(nombreDir):
    #contenido = os.listdir(ruta_base+nombreDir)
    contenido = obtenerSoloImagenes(ruta_base+nombreDir)
    arrImagenes = []
    for nombre_imagen in contenido:
        img = imread(ruta_base+nombreDir+'/'+nombre_imagen)    
        
        #Aplicamos el filtro Edge Roberts para quitar un poco las texturas de las ramas    
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
        imagen_actual = Imagen(nombreDir,fd, fNormRGB, fNormHSV)        
        #Se agrega al arreglo de caracteristicas de cada imagen
        arrImagenes.append(imagen_actual)
        
    return arrImagenes

    
directorios = obtenerDirectorios(ruta_base)
recorrerDirectorios(directorios)