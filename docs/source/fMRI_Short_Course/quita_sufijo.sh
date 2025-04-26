#!/bin/bash

dir=$(ls -1 *.rst.txt)

for ss in $dir
do
  fil=$(echo $ss | sed 's/.txt//')
  echo $fil
  mv $ss $fil
done



