
Introducción a la documentación de Don Clusterio!
================================================

referencia: `wiki <https://github.com/c13inb/c13inb.github.io/wiki/>`_


Ricardo Rios edited this page Mar 13, 2024 · `43 revisions <https://github.com/c13inb/c13inb.github.io/wiki/Home/_history>`_

Bienvenidos a la MRI-lab Wiki!
------------------------------

.. _target to paragraph:

Bienvenido a la wiki del **Laboratorio de Imágenes de Resonancia Magnética**. Esta página contiene el repositorio para la wiki y herramientas de los usuarios del MRI-lab.

    ⭐ No olvides también visitar la `wiki del Lanirem <https://github.com/lanirem/documentation/wiki/XCP-Preprocessing/>`_, donde puedes encontrar aún más información!

    ⚠️ Todo usuario del cluster Don Clusterio debe estar inscrito en la Red Lanirem en el canal `#don_clusterio <https://chat-lanirem.lavis.unam.mx/channel/don_clusterio/>`_. No hacerlo implica la desactivación de la cuenta.

Contenido en esta página
########################

.. contents:: Tabla de contenido
   :local:
   :backlinks: none
   :depth: 3

.. _My target:

MRILab Wiki
~~~~~~~~~~~~

Este wiki intenta facilitar el uso del clúster y las máquinas que lo forman. Cualquier persona puede consultar la wiki desde una computadora con acceso a internet.

Te invitamos a apoyar el desarrollo de esta wiki de las siguientes formas:

    - Si deseas complementar o corregir alguna entrada que ya está en la wiki.
    - Si aprendes algo nuevo y lo quieres incluir en esta wiki para que los demás podamos aprenderlo también.

Si deseas colaborar en esta wiki es necesario tener una cuenta de github y ser colaborador de este repositorio-wiki. Mas info en este link :doc:`Modificar-Wiki`


.. tabs::

   .. tab:: reStructuredText

      .. code-block:: rst

         .. _My target:

         Explicit targets
         ~~~~~~~~~~~~~~~~

         Reference `My target`_.

   .. tab:: MyST (Markdown)

      .. code-block:: md

         (My_target)=
         ## Explicit targets

         Reference [](My_target).




.. tabs::

   .. tab:: reStructuredText

      .. code-block:: rst

         .. _target to paragraph:

         An easy way is just to use the final link of the page/section.
         This works, but it has :ref:`some disadvantages <target to paragraph>`:

   .. tab:: MyST (Markdown)

      .. code-block:: md

         (target_to_paragraph)=

         An easy way is just to use the final link of the page/section.
         This works, but it has [some disadvantages](target_to_paragraph):





.. tabs::

   .. tab:: reStructuredText

      .. code-block:: rst

         You can also create _`in-line targets` within an element on your page,
         allowing you to, for example, reference text *within* a paragraph.



Advertencias
~~~~~~~~~~~~

Recuerda que el clúster es un sistema que depende de que los equipos que lo forman estén activos y en condiciones adecuadas.

    ⚠️Evita **reiniciar, apagar** o **desmontar** los equipos que se encuentre en el clúster.

    ⚠️Siempre es buena práctica hacer **Cerrar Sesión** al terminar el día.

    ⚠️ A veces no funciona bien el cambio de usuario y podrías perder datos. Acostúmbrate a **grabar tu progreso** con alta frecuencia para evitar tristes pérdidas.

    ⚠️ **Borra** continuamente la papelera de reciclaje

    ⚠️ Si se presenta algún problema que no esté contemplado en este wiki por favor **repórtalo al administrador** del sistema.




.. tabs::

   .. tab:: reStructuredText

      .. code-block:: rst

         For example, to reference the previous section
         you can use `Explicit targets`_.

   .. tab:: MyST (Markdown)

      .. code-block:: md

         For example, to reference the previous section
         you can use [](#explicit-targets).

      .. note::

         This requires setting ``myst_heading_anchors = 2`` in your ``conf.py``,
         see :ref:`myst-parser:syntax/header-anchors`.



Kit de supervivencia
~~~~~~~~~~~~~~~~~~~~


    - Aprende a buscar información
    - :doc:`Cluster`. Aquí se explica cómo está organizado el cluster, cómo se utiliza y los errores más frecuentes durante su uso.
    - :doc:`Modules` : Los módulos es una forma de cargar software a tu sesión de temrinal en el clúster. La mayoría de lso móludos están orientados a software de neuroimagen. Esta entrada explica como hacerlo.
    - :doc:`homeU` : ¿Qué es y cómo se usa?. En esta sección se mencionan las mejores prácticas para el uso de home en un sistema NFS, el uso de la carpeta temporal, cómo se realiza el respaldo home y el respaldo de los datos en general.
    - :doc:`misc` : ¿Dónde guardar mis datos?. Si bien /home guarda las configuraciones individuales de cada usuario, el respaldo de los datos (como las imágenes) debe realizarse en el directorio /misc con el fin de mejorar el uso del cluster.
    - :doc:`Bash` . Bash que es un programa informático cuya función es interpretar ordenes.
    - :doc:`Permisos` . Los permisos de lectura y escritura se deben de asignar tanto a carpetas como a archivos, ya que si los permisos no están debidamente asignados, puede derivar en un fallo en el procesamiento de la tarea por parte del cluster o en la falta de respaldo de los archivos.
    - :doc:`trabajoRemoto`. Cómo entrar al cluster desde tu laptop, en tu casa o en el café.
    - :doc:`ProcesamientoImagen` En esta sección se encuentran descritos los pasos para manipular los archivos de imagen (dicoms o niifti u otros). Aquí se describe como registrar, normalizar, transformar, reorientar, extraer, sumar, acoplar imágenes y más. Además de algunos enlaces a páginas interesantes.
    - :doc:`fmri`. Aprende a hacer análisis de resonancia funcional y algunas herramientas de fsl.
    - :doc:`bids`. Aprende acerca del estándar de almacenamiento de datos y cómo usar herramientas en contenedores.
    - Imágenes Pesadas a Difusión Asuntos relacionados a imágenes pesadas adifusión, su procesamiento y tractografía.
    - :doc:`Grosor_cortical` Información acerca del procesamiento de imágenes para la obtención del grosor cortical y otras bondades de FreeSurfer
    - Montar dropbox y similares con :doc:`rclone`
    - :doc:`FAQ-Trucos-Alertas`. Apuntes sobre algunas tareas que a los usuarios les han costado trabajo y no quiere que se les olviden, y para que potencialmente les sean útiles a otros usuarios.
    - :doc:`git`. Git es una herramienta que permite el control de versiones de código fuente.
    - Información adicional para el grupo :doc:`Bioinfo`.
    - :doc:`Amira` Es un software para visualización científica.
    - :doc:`Anaconda` Gesto de ambientes y paquetes de Python.




.. tabs::

   .. tab:: reStructuredText

      .. code-block:: rst

         For example, to reference the previous section
         you can use `Explicit targets`_.

   .. tab:: MyST (Markdown)

      .. code-block:: md

         For example, to reference the previous section
         you can use [](#explicit-targets).

      .. note::

         This requires setting ``myst_heading_anchors = 2`` in your ``conf.py``,
         see :ref:`myst-parser:syntax/header-anchors`.


Tutoriales Avanzados
~~~~~~~~~~~~~~~~~~~~

    - Grosor Cortical, por rcruces.
    - Procesamiento DWI, por rcruces.
    - Grosor Cortical con CIVET y FreeSurfer, por elidom




.. tabs::

   .. tab:: reStructuredText

      .. code-block:: rst

         For example, to reference the previous section
         you can use `Explicit targets`_.

   .. tab:: MyST (Markdown)

      .. code-block:: md

         For example, to reference the previous section
         you can use [](#explicit-targets).

      .. note::

         This requires setting ``myst_heading_anchors = 2`` in your ``conf.py``,
         see :ref:`myst-parser:syntax/header-anchors`.




