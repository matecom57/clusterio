## Grupo __bioinfo__ ##

### Datos
Los usuarios de este grupo pueden iniciar sesión al igual que los del grupo
fmriuser. Sin embargo con el afán de facilitar la labor de respaldo de los
diferentes grupos, es recomendable usar una carpeta por usuario en la carpeta
local de datos en específico, las que se encuentran en los equipos de bioinformática.

    /datos/equipo_bioinfo/usuario

Actualmente se cuenta con los equipos Opti790 y mendel.

### Permisos

A su vez es importante que el grupo y los [permisos](https://github.com/rcruces/C-13_wiki_demo/wiki/Permisos) de grupo se asignen tanto a carpetas como a archivos, ya que si los permisos no están debidamente asignados, esto puede derivar en un fallo en el procesamiento de la tarea por parte del clúster.

### Programas

Los programas se encuentran alojados en la carpeta:

    /datos/mendel/bioinfo/

Esto para permitir el acceso de todos los equipos del clúster a los programas.
Además algunas de las variables necesarias se asignan en un perfil que se
carga al inicio de sesión de cada usuario del grupo.

Los programas instalados son:

    Bowtie
    Bowtie2
    Tophat
    Cufflinks
    Bedtools
    HTseq
    Samtools
    Blat

Aún faltan por instalar y configurar:

    cummeRbund

### PATH y Variables

Para `bowtie2` se generó la variable BT2_HOME que señala a `/datos/mendel/bioinfo/bowtie2/`. Además las direcciones para las diferentes aplicaciones se encuentran en el path de los usuarios del grupo __bioinfo__. Por lo que en teoría cualquier aplicación de los paquetes se ejecutaría automáticamente para todos los usuarios.