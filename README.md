# Front-End Law&Tech

Projeto criado por alunos de graduação da Faculdade Senac Pernambuco, usando HTML, CSS, Javascript e [JSON Server](https://github.com/typicode/json-server).

É um sistema de gerenciamento de processos judiciais eletrônicos, com atualizações sobre as últimas movimentações processuais.

## Para rodar o servidor JSON (database)

Primeiro, instale o json-server via npm:

    npm install -g json-server

Depois, execute o seguinte comando para rodar o servidor:

    json-server --watch database.json

Se necessário, indicar o caminho completo onde está localizado o arquivo `database.json`.

O servidor irá rodar na porta 3000, sendo acessível pelo endereço:

    http://localhost:3000/

## Para rodar o site

Baixe as dependências necessárias:

    pip3 install -r requirements.txt

Execute o comando abaixo para rodar o site:

    python3 server.py

O site irá rodar na porta 5000, sendo acessível pelo endereço:

    http://localhost:5000/