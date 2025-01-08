#!/bin/bash

x="Bash_-Comandos-Básicos.md"

echo $x

x=$(echo $x | sed 's/á/a/g')
x=$(echo $x | sed 's/é/e/g')
x=$(echo $x | sed 's/í/i/g')
x=$(echo $x | sed 's/ó/o/g')
x=$(echo $x | sed 's/ú/u/g')
x=$(echo $x | sed 's/_-/-/g')
echo $x



