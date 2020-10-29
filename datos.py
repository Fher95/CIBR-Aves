# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:39:38 2020

@author: Packo
"""

import json
import numpy as np
from Imagen import Imagen

carpetaGuardado = 'Caracteristicas/'

def guardarVecImagenes(vecImagenes, nombreDirectorio):
    #Primero se vacía el archivo
    nombreDirectorio = carpetaGuardado+nombreDirectorio
    archivo = open (nombreDirectorio+'.json','w')
    archivo.write('')
    archivo.close()
    for objImagen in vecImagenes:
        guardarImagen(objImagen, nombreDirectorio)


def guardarImagen(objImagen, nombreDirectorio):
    
    vecRGB = objImagen.vecRGB.tolist()
    vecHSV = objImagen.vecHSV.tolist()
    vecHOG = objImagen.vecHOG.tolist()
    
    datos = {
        'nombreImg': objImagen.nombre,
        'vectorRGB': vecRGB,
        'vecHSV': vecHSV,
        'vecHOG': vecHOG        
    }
    
    datos = json.dumps(datos)
    
    esc = open(nombreDirectorio+'.json','a')
    esc.write(datos)
    esc.write("\n")
    esc.close()


    #LECTURA
    """
    lec =  open('datos.json', 'r')
    cadenas = lec.read()
    lec.close()
    lista = cadenas.split("\n")
    dato = json.loads(lista[0])
    print(dato["nombre"])
    """
