
Grosor cortical
===============

Luis Concha edited this page Mar 14, 2024 · 5 revisions

Grosor cortical

El grosor cortical es una medida dada por la distancia existente entre la superficie límite sustancia blanca y sustancia gris , y la superficie pial.
FreeSurfer

Es una plataforma desarrollada por el Hospital General de Massachusetts para el análisis de IRM. Facilita la visualización, el análisis volumétrico de algunas estructuras y la obtención del grosor cortical: http://freesurfer.net/
Deepprep

En marzo de 2024 apareció deepprep, que utiliza la GPU para acelerar muchos procesos. Instrucciones para correrlo como contenedor de singularity aquí.
Archivos a utilizar

Para el análisis del grosor cortical utilizando Freesurfer se necesitan imágenes tipo T1-3D. Pueden ser DICOMs o nifti.
Pasos para el análisis

    Crear carpeta “SUBJECTS_DIR” en la cual se depositaran todos los outputs de los análisis. Por ejemplo, se puede poner en una CarpetaA los dicoms e indicar que los outputs sean depositados en la Carpetab:

    /datos/maquina/usuario/CarpetaA$ export SUBJECTS_DIR=/datos/maquina/usuario/CarpetaB 

    Ahora se procede a asignar un nombre al sujeto, si es DICOM se usa el primero (a) o si es nifti, se usa toda la carpeta (b):

    a) recon-all  -all -subjid nombredelsujeto -i /datos/maquina/usuario/CarpetaA/nombredelsujeto/0001.dcm

    b) recon-all  -all -subjid nombredelsujeto -i /datos/maquina/usuario/CarpetaA/nombred

⚠️ A partir de enero de 2021 la versión por default es la 7.0.

⚠️ Muchos análisis se hicieron en el lab usando la versión 5.3, que ya no corre en ubuntu 18.04 por una discrepancia de perl. Por lo tanto, para correr la versión 5.3 es necesario hacerlo a través de un contenedor de singularity, que quedó grabado en /home/inb/lconcha/fmrilab_software/containers/freesurfer_5.3.sif. Para correr un sujeto, un puede usar, por ejemplo, el comando: singularity run /home/inb/lconcha/fmrilab_software/containers/freesurfer_5.3.sif recon-all -subjid XXXX -autorecon1

ℹ️ El gran Eliseo Domínguez hizo un magnífico tutorial que pueden ver en su github.
