from flask import Flask, request
import json
import base64
from PIL import Image
from io import BytesIO
import subprocess
from compararImagenes import recuperarContenidoImagen
from flask_cors import CORS, cross_origin
#from flask.ext.jsonpify import jsonify

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/prueba', methods=['GET'])
def cualquier():
    print('Entra a la prueba')
    return 'Maldito coso no funciona'
    
@app.route('/buscarImagen', methods=['POST'])
def pruebaPost():
    print('ENTRA AL POST DE BUSCAR IMAGEN...');
    req_data = request.get_json()
    strImg = req_data['base64img']    
    print('String recibido:', strImg)
    strImg = strImg.replace('data:image/jpeg;base64,','')
    im = Image.open(BytesIO(base64.b64decode(strImg)))
    im.save('imagenRecibida.jpg', 'JPEG')
    result = recuperarContenidoImagen('imagenRecibida.jpg')
    print('Data Result: ', result)
    result2 = convertirListaImagensAJson(result)
    print('RESULT2: ', result2)
    return result2

def convertirListaImagensAJson(vecImagenes):
    strRes = '{'
    for element in vecImagenes:
        obj = {'nombreGrupo': element[0], 'nombreImagen': element[1], 'distancia': element[2]}
        json_string = json.dumps(obj)
        strRes += json_string
        strRes += ','
    strRes = strRes[:-1]
    strRes += '}'
    return strRes


    

if __name__ == '__main__':
     app.run(port='5002')
