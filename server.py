from flask import Flask, render_template, redirect, request
import os 
from pathlib import Path
import platform

app = Flask(__name__)

# Porta padrão do flask
port = 5000
# Definindo a variável global usuarioId
usuarioId = 0
# Definindo se o usuário já está logado
usuarioEstaLogado = False
# Convertendo string 'True'/'False' para boolean
def str_to_bool(s):
    if s == 'True':
         return True
    elif s == 'False':
         return False
    else:
         raise ValueError

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/pages/login.html')
def login():
  if usuarioEstaLogado == False:
    return render_template('pages/login.html')
  elif usuarioEstaLogado == True:
    return render_template('pages/logout.html')

@app.route('/pages/cadastro.html')
def cadastro():
  if usuarioEstaLogado == False:
    return render_template('pages/cadastro.html')
  elif usuarioEstaLogado == True:
    return render_template('pages/logout.html')

@app.route('/pages/redefinir-senha.html')
def redefinir_senha():
  return render_template('pages/redefinir-senha.html')

@app.route('/pages/sobre.html')
def sobre():
  return render_template('pages/sobre.html')

@app.route('/pages/suporte.html')
def suporte():
  return render_template('pages/suporte.html')

@app.route('/user-login', methods=['POST'])
def user_login():
  # Obtendo as variáveis globais
  global usuarioEstaLogado
  # Obtendo os dados 
  data = request.data.decode('UTF-8')
  # Convertendo data para boolean
  usuarioEstaLogado = str_to_bool(data)

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
      plataforma = platform.system()
      # Linux
      if (plataforma == 'Linux'):
        os.system(f'python3 changedetection.py -d {path} -p {port+usuarioId}')
      # Windows
      elif (plataforma == 'Windows'):
        os.system(f'python -u changedetection.py -d {path} -p {port+usuarioId}')
    except OSError as error:
      print(error)

if __name__ == '__main__':
  # Usar uma porta específica, apenas se a porta padrão não funcionar
  # app.run(host='0.0.0.0', port=4999)
  app.run(debug=True)
  # Onde ficam armazenados os arquivos estáticos (CSS, JavaScript)
  app.static_folder = 'static'