# Bienvenidos a la MRI-lab Wiki!

Bienvenido a la wiki del **Laboratorio de Imágenes de Resonancia Magnética**. Esta página contiene el repositorio para la wiki  y herramientas de los usuarios del MRI-lab.



> :star: No olvides también visitar la [wiki del Lanirem](https://github.com/lanirem/documentation/wiki/XCP-Preprocessing), donde puedes encontrar aún más información!

> :warning: Todo usuario del cluster Don Clusterio debe estar inscrito en la Red Lanirem en el canal [#don_clusterio](https://chat-lanirem.lavis.unam.mx/channel/don_clusterio). No hacerlo implica la desactivación de la cuenta.

# Contenido en esta página
1. [MRILab Wiki](#mrilab-wiki)
1. [Advertencias](#advertencias)
1. [Kit de supervivencia](#kit-de-supervivencia)
1. [Tutoriales Avanzados](#tutoriales-avanzados)

## MRILab Wiki
Este wiki intenta facilitar el uso del clúster y las máquinas que lo forman. Cualquier persona puede consultar la wiki desde una computadora con acceso a internet.

Te invitamos a apoyar el desarrollo de esta wiki de las siguientes formas:
1. Si deseas complementar o corregir alguna entrada que ya está en la wiki.
1. Si aprendes algo nuevo y lo quieres incluir en esta wiki para que los demás podamos aprenderlo también.

Si deseas colaborar en esta wiki es necesario tener una cuenta de github y ser colaborador de este repositorio-wiki. Mas info en este [link](./Modificar-Wiki)

## Advertencias
Recuerda que el clúster es un sistema que depende de que los equipos que lo forman estén activos y en condiciones adecuadas.
>  :warning:Evita **reiniciar**, **apagar** o **desmontar** los equipos que se encuentre en el clúster.

>  :warning:Siempre es buena práctica hacer **Cerrar Sesión** al terminar el día.

>  :warning: A veces no funciona bien el cambio de usuario y podrías perder datos. Acostúmbrate a **grabar tu progreso** con alta frecuencia para evitar tristes pérdidas.

>  :warning: **Borra** continuamente la papelera de reciclaje


>  :warning: Si se presenta algún problema que no esté contemplado en este wiki por favor **repórtalo al administrador** del sistema.


## Kit de supervivencia
+ *Aprende a buscar información*
+ [[Clúster]]. Aquí se explica cómo está organizado el cluster, cómo se utiliza y los errores más frecuentes durante su uso.
+ [Modulos](./Modules): Los módulos es una forma de cargar software a tu sesión de temrinal en el clúster. La mayoría de lso móludos están orientados a software de neuroimagen. Esta entrada explica como hacerlo.
+ [/home](./Clúster:-Folder-usuario-(home)): *¿Qué es y cómo se usa?*. En esta sección se mencionan las mejores prácticas para el uso de `home` en un sistema __NFS__, el uso de la carpeta [temporal](./Clúster:-Folder-temporal-(tmp)), cómo se realiza el [respaldo home](./Clúster:-Respaldo-de-datos) y el respaldo de los [datos](./Clúster:-Folder-almacenamiento-(misc)) en general.
+ [/misc](./Clúster:-Folder-almacenamiento-(misc)): *¿Dónde guardar mis datos?*. Si bien `/home` guarda las configuraciones individuales de cada usuario, el respaldo de los datos (como las imágenes) debe realizarse en el directorio `/misc` con el fin de mejorar el uso del cluster.
+ [[Bash]]. **Bash** que es un programa informático cuya función es interpretar ordenes.
+ [Permisos](./Bash:-Permisos). Los permisos de lectura y escritura se deben de asignar tanto a carpetas como a archivos, ya que si los permisos no están debidamente asignados,  puede derivar en un fallo en el procesamiento de la tarea por parte del cluster o en la falta de respaldo de los archivos.
+ [Trabajo remoto](./trabajoRemoto). Cómo entrar al cluster desde tu laptop, en tu casa o en el café.
+ [Tutoriales básicos de manipulación y procesamiento de imágenes](./Procesamiento-Imagen) En esta sección se encuentran descritos los pasos para manipular los archivos de imagen (dicoms o niifti u otros). Aquí se describe como registrar, normalizar, transformar, reorientar, extraer, sumar, acoplar imágenes y más. Además de algunos enlaces a páginas interesantes.
+ [fMRI](./fMRI). Aprende a hacer análisis de resonancia funcional y algunas herramientas de [[fsl]].
+ [BIDS](./BIDS). Aprende acerca del estándar de almacenamiento de datos y cómo usar herramientas en contenedores.
+ [Imágenes Pesadas a Difusión](./DWMEI)
Asuntos relacionados a imágenes pesadas adifusión, su procesamiento y tractografía.
+ [Grosor Cortical](https://github.com/c13inb/c13inb.github.io/wiki/Grosor-cortical) Información acerca del procesamiento de imágenes para la obtención del grosor cortical y otras bondades de **FreeSurfer**
+ Montar dropbox y similares con [[rclone]]
+ [[FAQ, Trucos y Alertas]] Preguntas frecuentes. Apuntes sobre algunas tareas que a los usuarios les han costado trabajo y no quiere que se les olviden, y para que potencialmente les sean útiles a otros usuarios.
+ [[git]]. **Git** es una herramienta que permite el control de versiones de [código fuente](https://en.wikipedia.org/wiki/Source_code).
+ Información adicional para el grupo [[BIOINFO]].
+ [[Amira]] Es un software para visualización científica.
+ [[Anaconda]] Gesto de ambientes y paquetes de Python.


## Tutoriales Avanzados
1. [Grosor Cortical](https://github.com/rcruces/MRI_analytic_tools/tree/master/Freesurfer_preprocessing), por rcruces.
1. [Procesamiento DWI](https://github.com/rcruces/MRI_analytic_tools/tree/master/DWI_preprocessing), por rcruces.
3. [Grosor Cortical con CIVET y FreeSurfer](https://elidom.github.io/Cortical-Thickness/), por elidom

## Enlaces externos
+ [Enlaces Interesantes](https://github.com/c13inb/c13inb.github.io/wiki/Enlaces) con diversas herramientas.
+ [[Histología]]. Links externos con diversas herramientas.
