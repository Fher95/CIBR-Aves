from flask import Flask, request
import json
import base64
from PIL import Image
from io import BytesIO
import subprocess
from compararImagenes import recuperarContenidoImagen

#from flask.ext.jsonpify import jsonify

app = Flask(__name__)


@app.route('/prueba', methods=['GET'])
def cualquier():
    print('Entra a la prueba')
    return 'Maldito coso no funciona'
    
@app.route('/buscarImagen', methods=['POST'])
def pruebaPost():
    # print('ENTRA AL POST');
    # req_data = request.get_json()
    # strImg = req_data['base64img']
    # print('String recibido:', strImg)
    # strImg = strImg.replace('data:image/jpeg;base64,','')
    # im = Image.open(BytesIO(base64.b64decode(strImg)))
    # im.save('imagenRecibida.jpg', 'JPG')
    # result = recuperarContenidoImagen('imagenRecibida.jpg')
    # print('Data Recibida: ', result)
    # return result
    print('Cualquier cosa')
    return 'Cualquier cosa'

def convertirListaImagensAJson(vecImagenes):
    for element in vecImagenes:
        obj = {nombreGrupo: element[0]}

    

if __name__ == '__main__':
     app.run(port='5002')
