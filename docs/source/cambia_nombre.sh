#!/bin/bash

dir=$(ls -1)

for dd in $dir
do 
  y=${dd: -3}
  if [ "$y" == ".md" ]
  then
    x=${dd}
    echo $x
    x=$(echo $x | sed -e 's/ú/u/g')
    x=$(echo $x | sed -e 's/ó/o/g')
    x=$(echo $x | sed -e 's/á/a/g')
    x=$(echo $x | sed -e 's/í/i/g')
    x=$(echo $x | sed -e 's/_-/-/g')
    x=$(echo $x | sed -e 'y/áéíóú/aeiou/')
    len=${#x}
    w=${x: 0: len-3}
    nom=$w".rst"
    echo $nom
    cp $dd $nom
  fi
done



