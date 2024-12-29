Matlab corre sin problemas en el cluster usando su interfaz gráfica. La mayoría de los usuarios trabajan en matlab en solo una PC, pero hay ocasiones en que uno quisiera paralelizar código de matlab a través del cluster. Bueno, pues la manera oficial de hacerlo es con matlab pools, pero eso no está configurado (aún) en Don Clusterio. Sin embargo, si el tipo de problema se presta, podemos hacer un truco simpático para encapsular código de matlab en funciones de bash que se manden como trabajos en el cluster con SGE. Veamos un ejemplo:

## Encapsular matlab en bash

Haré un script de bash llamado `corre_matlab.sh`, que usará matlab para calcular el promedio de dos números. Lo sé, un ejemplo muy simplón, pero ya imaginarás que este ejemplo se puede modificar para códigos tan complicados como una película de Christopher Nolan.

```bash
#!/bin/bash
A=$1
B=$2

matlab_job=/tmp/m2d_$$_matlab_job.m
echo "addpath('/misc/mansfield/lconcha/scripts');" >> $matlab_job
echo "av = mean([${A} ${B}])" >> $matlab_job
echo "exit" >> $matlab_job

cat $matlab_job

matlab -nojvm -nodesktop < $matlab_job

rm -f $matlab_job
```


Veamos qué está pasando:

El script de bash recibirá dos argumentos, que asignará a variables `$A` y `$B`. 

Se generará un archivo de texto que contendrá los comandos de matlab. Las líneas con `echo` agregan los comandos de matlab. Si es necesario, agregamos cosas al `path` de matlab ahí. En el tercer `echo` se ve cómo se sustituyen las variables `$A` y `$B` (de bash) dentro de una función simple de matlab. 

La penúltima línea corre matlab sin GUI. Si el script de matlab hubiera escrito archivos, matlab se habría encargado de hacerlo, no bash.

Finalmente se borra el script temporal de matlab.

## Corriendo el script en el cluster.

Ahora, para correr esto en el cluster, sería sencillo:

1. Nos aseguramos de estar corriendo la última versión de fsl (fsl 6.0.2 o 6.0.5), pues aprovecharemos su gestor de SGE (`fsl_sub`). 
2. Dado que el script de prueba  se llama `corre_matlab.sh`, entonces enviamos al cluster así

```bash
PRIMERO=10
SEGUNDO=20
fsl_sub -N nombreDelJob -l /ruta/para/logs ./corre_matlab.sh $PRIMERO $SEGUNDO
```