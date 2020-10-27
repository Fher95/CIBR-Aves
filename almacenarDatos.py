# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:39:38 2020

@author: Packo
"""

import json
import numpy as np

def guardar(vectorCaracteristicas):
    
    vectorCaracteristicas = np.array(vectorCaracteristicas)
    vectorCaracteristicas = vectorCaracteristicas.tolist()
    
    datos = {
        'vector': vectorCaracteristicas
    }
    
    datos = json.dumps(datos)
    
    esc = open('datos.json','a')
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
