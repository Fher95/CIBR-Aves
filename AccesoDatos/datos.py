import json
import numpy as np
from .Imagen import Imagen
import os

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
        'nombreGrupo': objImagen.nombreGrupo,
        'vectorRGB': vecRGB,
        'vecHSV': vecHSV,
        'vecHOG': vecHOG        
    }
    
    datos = json.dumps(datos)
    
    esc = open(nombreDirectorio+'.json','a')
    esc.write(datos)
    esc.write("\n")
    esc.close()

def leerDatos():
    datos = []
    contenido = os.listdir('Caracteristicas')
    archivos = [nombre for nombre in contenido]
    for i in archivos:
        lec = open('Caracteristicas/'+i, 'r')
        dato = lec.read();
        lista = dato.split("\n")
        lista.pop()
        for j in lista:
           datos.append(json.loads(j))
        
    return datos
    
    #LECTURA
    """
    lec =  open('datos.json', 'r')
    cadenas = lec.read()
    lec.close()
    lista = cadenas.split("\n")
    dato = json.loads(lista[0])
    print(dato["nombre"])
    """
