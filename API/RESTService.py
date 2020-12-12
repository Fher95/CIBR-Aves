from flask import Flask, request
import json
import base64
from PIL import Image
from io import BytesIO
from Logica.compararImagenes  import recuperarContenidoImagen
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def convertirListaImagensAJson(parLista):
    {'topImagenes': {}, 'topGrupos': {} }
    strRes = '['
    for element in parLista:
        obj = {}
        if len(element) == 3:
            obj = {'nombreGrupo': element[0], 'nombreImagen': element[1], 'distancia': element[2]}
        else:
            obj = {'nombreGrupo': element[0], 'numeroOcurrencias': element[1]}
        json_string = json.dumps(obj)
        strRes += json_string
        strRes += ','
    strRes = strRes[:-1]
    strRes += ']'
    return strRes

def crearRespuesta(lista1,lista2):
    strTopImagenes = convertirListaImagensAJson(lista1)
    strTopGrupos = convertirListaImagensAJson(lista2)        
    objRes = {'topImagenes': json.loads(strTopImagenes), 'topGrupos': json.loads(strTopGrupos)}
    strRes = json.dumps(objRes)
    return objRes;
    
@app.route('/buscarImagen', methods=['POST'])
def pruebaPost():
    print('Comenzando proceso de recuperación de imagenes...');
    req_data = request.get_json()
    strImg = req_data['base64img']    
    strImg = strImg.replace('data:image/jpeg;base64,','')
    im = Image.open(BytesIO(base64.b64decode(strImg)))
    im.save('imagenRecibida.jpg', 'JPEG')
    topImagenes, topGrupos = recuperarContenidoImagen('imagenRecibida.jpg')    
    result = crearRespuesta(topImagenes,topGrupos) 
    print('Finalizada recuperación de imagenes. Enviando resultados. ')
    return result

def iniciarServer():
    app.run(port='5002')


