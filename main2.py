from flask import Flask, request, Response

app = Flask(__name__)
PATH_TO_TEST_IMAGES_DIR = './subidos'

@app.route('/')
def index():
    return Response('<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta http-equiv="X-UA-Compatible" content="ie=edge" /><title>Subidor de Imagenes PNG</title></head><body><h3> :5000 <h3><hr><form enctype="multipart/form-data" action="upload" method="post"><p> Nombre:	<input type="text" name="Nombre" /> </p><p> Archivo:	<input type="file" name="Archivo" /> </p><input type="submit" value="upload" /></form></body></html>', mimetype='text/html')

@app.route('/upload', methods=['POST'])
def image():
    variable = request.form.get('Nombre')
    file = request.files['Archivo']
    fragmentar = file.filename.split(".")
    extension = fragmentar[-1]
    if file.filename != '':
        file.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, variable+"."+extension))
        print('Subida Completada '+file.filename+' y renombrado '+variable+"."+extension)
        return Response('Subida Completada '+file.filename+' y renombrado '+variable+"."+extension)
    else:
        print('Error al obtener el archivo del cliente')
        return Response('Variable Nombre: '+variable+' \n<br>Error al obtener el archivo el servidor')


if __name__ == '__main__':
    app.run()
