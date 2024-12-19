¡Bienvenido a la documentación de Don Clusterio!
===================================

referencia: `wiki <https://github.com/c13inb/c13inb.github.io/wiki/>`_


Home

Ricardo Rios edited this page Mar 13, 2024 · `43 revisions <https://github.com/c13inb/c13inb.github.io/wiki/Home/_history>`_

Bienvenidos a la MRI-lab Wiki!
------------------------------

Bienvenido a la wiki del **Laboratorio de Imágenes de Resonancia Magnética**. Esta página contiene el repositorio para la wiki y herramientas de los usuarios del MRI-lab.

    ⭐ No olvides también visitar la `wiki del Lanirem <https://github.com/lanirem/documentation/wiki/XCP-Preprocessing/>`_, donde puedes encontrar aún más información!

    ⚠️ Todo usuario del cluster Don Clusterio debe estar inscrito en la Red Lanirem en el canal `#don_clusterio <https://chat-lanirem.lavis.unam.mx/channel/don_clusterio/>`_. No hacerlo implica la desactivación de la cuenta.

Contenido en esta página
------------------------

.. toctree::
    :maxdepth:2
    :caption: Contenido

    MRILab Wiki :ref:`mrilabwiki`
    Advertencias
    Kit de supervivencia
    Tutoriales Avanzados

.. _mrilabwiki:

MRILab Wiki

Este wiki intenta facilitar el uso del clúster y las máquinas que lo forman. Cualquier persona puede consultar la wiki desde una computadora con acceso a internet.

Te invitamos a apoyar el desarrollo de esta wiki de las siguientes formas:

    Si deseas complementar o corregir alguna entrada que ya está en la wiki.
    Si aprendes algo nuevo y lo quieres incluir en esta wiki para que los demás podamos aprenderlo también.

Si deseas colaborar en esta wiki es necesario tener una cuenta de github y ser colaborador de este repositorio-wiki. Mas info en este link
Advertencias

Recuerda que el clúster es un sistema que depende de que los equipos que lo forman estén activos y en condiciones adecuadas.

    ⚠️Evita reiniciar, apagar o desmontar los equipos que se encuentre en el clúster.

    ⚠️Siempre es buena práctica hacer Cerrar Sesión al terminar el día.

    ⚠️ A veces no funciona bien el cambio de usuario y podrías perder datos. Acostúmbrate a grabar tu progreso con alta frecuencia para evitar tristes pérdidas.

    ⚠️ Borra continuamente la papelera de reciclaje

    ⚠️ Si se presenta algún problema que no esté contemplado en este wiki por favor repórtalo al administrador del sistema.

Kit de supervivencia

    Aprende a buscar información
    Clúster. Aquí se explica cómo está organizado el cluster, cómo se utiliza y los errores más frecuentes durante su uso.
    Modulos: Los módulos es una forma de cargar software a tu sesión de temrinal en el clúster. La mayoría de lso móludos están orientados a software de neuroimagen. Esta entrada explica como hacerlo.
    /home: ¿Qué es y cómo se usa?. En esta sección se mencionan las mejores prácticas para el uso de home en un sistema NFS, el uso de la carpeta temporal, cómo se realiza el respaldo home y el respaldo de los datos en general.
    /misc: ¿Dónde guardar mis datos?. Si bien /home guarda las configuraciones individuales de cada usuario, el respaldo de los datos (como las imágenes) debe realizarse en el directorio /misc con el fin de mejorar el uso del cluster.
    Bash. Bash que es un programa informático cuya función es interpretar ordenes.
    Permisos. Los permisos de lectura y escritura se deben de asignar tanto a carpetas como a archivos, ya que si los permisos no están debidamente asignados, puede derivar en un fallo en el procesamiento de la tarea por parte del cluster o en la falta de respaldo de los archivos.
    Trabajo remoto. Cómo entrar al cluster desde tu laptop, en tu casa o en el café.
    Tutoriales básicos de manipulación y procesamiento de imágenes En esta sección se encuentran descritos los pasos para manipular los archivos de imagen (dicoms o niifti u otros). Aquí se describe como registrar, normalizar, transformar, reorientar, extraer, sumar, acoplar imágenes y más. Además de algunos enlaces a páginas interesantes.
    fMRI. Aprende a hacer análisis de resonancia funcional y algunas herramientas de fsl.
    BIDS. Aprende acerca del estándar de almacenamiento de datos y cómo usar herramientas en contenedores.
    Imágenes Pesadas a Difusión Asuntos relacionados a imágenes pesadas adifusión, su procesamiento y tractografía.
    Grosor Cortical Información acerca del procesamiento de imágenes para la obtención del grosor cortical y otras bondades de FreeSurfer
    Montar dropbox y similares con rclone
    FAQ, Trucos y Alertas Preguntas frecuentes. Apuntes sobre algunas tareas que a los usuarios les han costado trabajo y no quiere que se les olviden, y para que potencialmente les sean útiles a otros usuarios.
    git. Git es una herramienta que permite el control de versiones de código fuente.
    Información adicional para el grupo BIOINFO.
    Amira Es un software para visualización científica.
    Anaconda Gesto de ambientes y paquetes de Python.

Tutoriales Avanzados

    Grosor Cortical, por rcruces.
    Procesamiento DWI, por rcruces.
    Grosor Cortical con CIVET y FreeSurfer, por elidom

Enlaces externos

    Enlaces Interesantes con diversas herramientas.
    Histología. Links externos con diversas herramientas.

Pages 108

Tabla de contenidos

    Home
    Como colaborar en la Wiki
    rocket.chat
    Resonadores
        Bruker
        GE
        Philips
    Bash
        Comandos Básicos
        Avanzado
    Clúster
        Organización de datos
        Respaldo de datos
        Gestión de procesos
        Módulos
        Uso del clúster
        Errores del clúster
        Agilizando tu sesión
    Procesamiento de Imágenes
        Herramientas
            FSL
            MRtrix3
            FreeSurfer
            BIDS
        Transformación de datos
    fMRI
        FEAT
        fMRI en roedores
        Conectividad Funcional Basada en Semilla
    DW-MRI
        Preprocesamiento humanos.
        Preprocesamiento roedores.
        Tractografía
        Multi-tensor
        Registro
        DSIstudio
    FIJI - Análisis histológico
        Tensor de Estructura
        Stitching
    Herramientas Software
        rclone
        X2Go
        SSH
        Git
        Anaconda
    Otros
        markdown

Clone this wiki locally
Footer
