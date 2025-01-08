#!/bin/bash
dir=$(ls -1)
for dd in $dir
do
#  echo $dd
  if [ -d $dd ]
  then
    echo "es directorio - "$dd
  fi
done

