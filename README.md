# Projeto Law&Tech (sistema de notificação JusUpdate)

Projeto criado por alunos de graduação da Faculdade Senac Pernambuco, usando HTML, CSS, Javascript, Python (Flask) e [JSON Server](https://github.com/typicode/json-server).

É um sistema de gerenciamento de processos judiciais eletrônicos, com atualizações sobre as últimas movimentações processuais.

## Para clonar o repositório

    git clone https://github.com/renanleitev/lawtech-backend.git

## Para atualizar o projeto

    git pull

## Primeiros passos

Antes de tudo, é preciso criar uma pasta chamada 'datastore' no diretório atual. Só é preciso fazer uma vez, quando houver clonado este repositório.

A pasta chamada 'datastore' é onde ficarão salvos as URLs armazenadas para checagem de atualizações.

    mkdir datastore

## Para rodar o servidor JSON (database)

Primeiro, instale o json-server via npm:

    npm install -g json-server

Depois, execute o seguinte comando para rodar o servidor:

    json-server --watch database.json

Se necessário, indicar o caminho completo onde está localizado o arquivo `database.json`.

O servidor irá rodar na porta 3000, sendo acessível pelo endereço:

    http://localhost:3000/

Caso a porta 3000 esteja ocupada, rodar o servidor na próxima porta disponível (3001, 3002, ...):

    json-server --watch database.json -p 3002

Após, executar o script bash "change-port.sh" e passar os seguintes argumentos:

    ./change-port.sh {nome-arquivo.html} {porta-json-server}
    
Exemplo:
    
    ./change-port.sh login.html 3002

Obs: Não feche o terminal. Deixe o JSON Server rodando, para poder acessar o banco de dados.

## Para rodar o site

Primeiro, abra um novo terminal. Deixe o JSON Server rodando, para poder acessar o banco de dados.  

Depois, instale o Python e o Pip na sua máquina:

Windows:
   
1. Python: 

        https://www.python.org/downloads/

2. Pip: 

        https://pip.pypa.io/en/stable/installation/

Linux:

1. Python: 

        sudo apt-get install python3

2. Pip: 
    
        sudo apt-get install python3-pip  


Baixe as dependências necessárias:

1. Windows:

        pip install -r requirements.txt

2. Linux:

        pip3 install -r requirements.txt

Abra um novo terminal e execute o comando abaixo para rodar o site:

1. Windows:

        python -u server.py

2. Linux:

        python3 server.py

O site irá rodar na porta 5000, sendo acessível pelo endereço:

    http://localhost:5000/

Obs: É preciso rodar tanto o JSON Server quanto o server.py, caso contrário o projeto não funciona.

## Script para executar o banco de dados e o site (Linux)

Se estiver executando as configurações padrões (JSON Server = 3000 / Flask = 5000), basta executar o script abaixo para rodar o banco de dados e o site:

    ./run-project.sh

## TODO

1. Criar banco de dados, para armazenar os dados dos usuários  
2. Encriptar a senha dos usuários
3. <s>Criar um sistema de logout, para o usuário poder sair do sistema</s> FEITO
4. <s>Criar mais páginas sobre o produto</s> FEITO
5. <s>Descrever o passo a passo de utilização do sistema</s> FEITO