#!/bin/bash

# $1 = nome do arquivo html
# $2 = número da porta do JSON Server

# caminho=$(readlink -f $1)

caminho="$(cd "$(dirname "$1")" && pwd -P)/templates/pages/$(basename "$1")"

sed -i "s/localhost:3000/localhost:$2/" $caminho