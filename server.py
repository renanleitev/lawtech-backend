from flask import Flask, render_template, redirect, request
import os 
from pathlib import Path

app = Flask(__name__)

# Porta padrão do flask
port = 5000
# Definindo a variável global usuarioId
usuarioId = 0


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/pages/login.html')
def login():
  # Obtendo as variáveis globais
  global port
  global usuarioId
  # Porta padrão do flask
  port = 5000
  # Definindo a variável global usuarioId
  usuarioId = 0
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

@app.route('/create-instance', methods=['POST'])
def create_instance():
    # Obtendo as variáveis globais
    global port
    global usuarioId
    # Obtendo os dados em formato JSON e convertendo para dicionário
    data = eval(request.data.decode('UTF-8'))
    # Obtendo o id do usuário
    usuarioId = int(data['usuarioId'])
    # Pasta onde serão armazenadas as URLs, padrão é 'datastore'
    allDataStored = 'datastore'
    # Obtendo o caminho absoluto da pasta atual
    absolutePath = Path().absolute()
    # Caminho onde serão armazenados os dados do usuário
    path = f'{absolutePath}/{allDataStored}/{usuarioId}'
    try: 
      # Tenta criar a pasta, caso ela não exista
      os.mkdir(path)
    except OSError as error: 
      print(error)
    try:
      # Iniciando uma instância do JusUpdate
      os.system(f'python3 changedetection.py -d {path} -p {port+usuarioId}')
    except OSError as error:
      print(error)
    # Redirecionando para a rota '/jusupdate'
    return redirect('/jusupdate')

@app.route('/jusupdate')
def jusupdate():
    # Obtendo as variáveis globais
    global port
    global usuarioId
    # Redirecionando para a instância do JusUpdate
    return redirect(f'http://localhost:{port+usuarioId}/')

if __name__ == '__main__':
  # Usar uma porta específica, apenas se a padrão não funcionar
  # app.run(host='0.0.0.0', port=4999)
  app.run(debug=True)
  # Onde ficam armazenados os arquivos estáticos (CSS, JavaScript)
  app.static_folder = 'static'