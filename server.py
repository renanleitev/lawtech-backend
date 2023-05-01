from flask import Flask, render_template, redirect, request
import os 
from pathlib import Path
import random

app = Flask(__name__)

port = random.randrange(65535)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/pages/login.html')
def login():
  return render_template('pages/login.html')

@app.route('/pages/cadastro.html')
def cadastro():
  return render_template('pages/cadastro.html')

@app.route('/pages/sobre.html')
def sobre():
  return render_template('pages/sobre.html')

@app.route('/pages/suporte.html')
def suporte():
  return render_template('pages/suporte.html')

@app.route('/create-folder', methods=['POST'])
def create_folder():
    global port
    port = random.randrange(65535)
    data = request.data.decode('UTF-8')
    allDataStored = 'datastore'
    absolutePath = Path().absolute()
    path = f'{absolutePath}/{allDataStored}/{data}'
    try: 
      os.mkdir(path)
    except OSError as error: 
      print(error)
    try:
      os.system(f'python3 changedetection.py -d {path} -p {port}')
    except OSError as error:
      print(error)
    return redirect('/jusupdate')

@app.route('/jusupdate')
def jusupdate():
    global port
    return redirect(f'http://localhost:{port}/')

if __name__ == '__main__':
  # Usar uma porta específica, apenas se a padrão não funcionar
  # app.run(host='0.0.0.0', port=4999)
  app.run(debug=True)
  app.static_folder = 'static'