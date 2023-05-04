#!/bin/bash

# $1 = nome do arquivo html
# $2 = número da porta do JSON Server

# caminho=$(readlink -f $1)

# caminho="$(cd "$(dirname "$1")" && pwd -P)/templates/pages/$(basename "$1")"

sed -i "s/localhost:3000/localhost:$1/" caminho="$(cd "$(dirname "login.html")" && pwd -P)/templates/pages/$(basename "login.html")";

sed -i "s/localhost:3000/localhost:$1/" caminho="$(cd "$(dirname "cadastro.html")" && pwd -P)/templates/pages/$(basename "cadastro.html")";

sed -i "s/localhost:3000/localhost:$1/" caminho="$(cd "$(dirname "redefinir-senha.html")" && pwd -P)/templates/pages/$(basename "redefinir-senha.html")";

sed -i "s/localhost:3000/localhost:$1/" caminho="$(cd "$(dirname "redefinir-senha.html")" && pwd -P)/templates/pages/$(basename "redefinir-senha.html")"