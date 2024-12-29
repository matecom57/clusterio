
# fmriprep


[fMRIPrep](https://fmriprep.readthedocs.io/en/stable/) es una herramienta desarrollada por el grupo de Russ Poldrack que tiene como objetivo el pre-procesamiento de datos de resonancia funcional (BOLD) para su posterior análisis mediante otras herramientas. El pre-procesamiento de los datos es crucial para cualquier análisis de BOLD, ya sea de tareas, o de resting-state. Existe mucha controversia de cómo deben pre-procesarse los datos (ver, [por ejemplo](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5489207/)), pues algunas elecciones pueden llevar a diferentes resultados. fMRIPrep facilita la tarea de pre-procesamiento y ofrece varias alternativas que pueden calcularse de forma simultánea, facilitando la tarea del proceso de múltiples versiones de análisis.

> :star: No olvides visitar este otro [tutorial](https://github.com/lanirem/documentation/wiki/FMRIPREP-preprocessing) para correr fmriprep en el LAVIS.

Una vez que los datos están organizados en formato [BIDS](./BIDS), podemos utilizar [Singularity](https://singularity.lbl.gov/) para correr fMRIPrep. Además, utilzando el cluster, que está administrado mediante [SGE](https://es.wikipedia.org/wiki/Sun_Grid_Engine), se pueden correr varios sujetos de manera paralela. Para facilitar la vida, el script `fsl_sub` encapsula los comandos necesarios para la utilización del cluster SGE.


>  :warning:Si vas a correr muchos sujetos de forma simultánea, **existe el riesgo de que satures el cluster.**. Para evitarlo puedes hacer dos cosas:
1. Envía tus sujetos de diez en diez.
2. Solicita mucho RAM para cada uno de los trabajos utilizando el switch `-R` de `fsl_sub`.


Aquí abajo hay un ejemplo de un script para enviar a analizar a un grupo de sujetos. En el ejemplo, la carpeta BIDS (asignada a la variable `bidsDir`) tiene a los sujetos con nomenclatura `sub-????`, donde cada `?` indica un dígito. Es decir, hay desde el sujeto `sub-0001` hasta potencialmente el `sub-9999`. Entonces, para enviar a los sujetos `sub-0001` al `sub-0009`, podemos poner que se procesen los sujetos `${bidsDir}/sub-000?` en la línea donde generamos la lista de sujetos a procesar.

Como vemos en la línea que invoca a `fsl_sub`, estamos solicitando 8 GB de RAM para cada trabajo (`-R 8`), y en las opciones que pasamos a fmriprep, pedimos que el máximo de memoria sean 6000 MB (`--mem_mb 7000`). Como medida adicional, pedimos que cada trabajo no utilice más de un CPU con `--nthreads 1`. Estos detallitos harán que los usuarios de las computadoras no se enojen con nosotros porque estemos acabándonos los recursos de sus máquinas.

```bash
#!/bin/bash

## Indicamos los lugares donde están los datos.
## Ojo, todos deben estar en algún lugar dentro de /misc
# 1. El contenedor de fmriprep
container=/misc/mansfield/lconcha/containers/fmriprep.img
# 2. La ruta de los datos en formato BIDS
bidsDir=/misc/mansfield/lconcha/bids/datos_Circe
# 3. La ruta donde poner los resultados
outDir=/misc/mansfield/lconcha/TMP/out/test
# 4. Una ruta para archivos temporales
workDir=/misc/mansfield/lconcha/TMP/work



# Necesitamos una licencia de freesurfer
export FS_LICENSE=${FREESURFER_HOME}/.license

# Generamos la lista de sujetos a procesar
subjid=`ls -d ${bidsDir}/sub-000?`

# Enviamos los jobs de uno por uno al cluster.
for s in $subjid
do
  this_subject=`basename $s`
  this_subject=${this_subject/sub-/}
  echo "submitting job for subject $this_subject"
  fsl_sub -N pre_${this_subject} -R 8 \
  singularity run \
  --bind /misc $container \
  ${bidsDir} \
  $outDir \
  participant \
  --participant_label $this_subject \
  --fs-no-reconall \
  --ignore fieldmaps \
  --output-space template \
  -w $workDir \
  --resource-monitor \
  --write-graph \
  --fs-license $FS_LICENSE \
  --nthreads 1 \
  --mem_mb 7000
  echo ""
  sleep 1
done
```

Por supuesto, esto es solo un ejemplo, y la miríada de opciones de fMRIPrep pueden consultarse en el [respectivo manual](https://fmriprep.readthedocs.io/en/stable/).


# Revisar el output
`fmriprep` escribe muchos archivos, pero es muy fácil revisar el resultado a través de una página .html que crea por cada sujeto en la carpeta `$outDir`. Es tan sencillo como ir a la carpeta donde están los .html y dar clic en ellos para que se abran en un navegador.

Yo soy muy flojo, por lo que abro de diez en diez como pestañas en el navegador. Por ejemplo, como `outDir=/misc/mansfield/lconcha/TMP/out/test`, entonces puedo escribir en la terminal:
```
chromium-browser ${outDir}/fmriprep/sub-001?.html
```
y voy a ver los reportes del sujeto `sub-0010` al `sub-0019`.

:star:  Esto funciona incluso mediante `sshfs`!
