Bash: Comandos Básicos -2
====================


Lista de comandos:
--------------------


man = manual
--------------------

La gran mayoria de los comandos vienen con un manual de uso, para acceder a estos hay que utilizar ``man`` y despues escribir el nombre del comando que quieres aprender a usar:

.. code-block:: Bash 

   man echo
   
   NAME
          echo - display a line of text
   
   SYNOPSIS
          echo [SHORT-OPTION]... [STRING]...
          echo LONG-OPTION
   
   DESCRIPTION
          Echo the STRING(s) to standard output.
   
          -n     do not output the trailing newline
   
          -e     enable interpretation of backslash escapes
   
          -E     disable interpretation of backslash escapes (default)
   
          --help display this help and exit
   
          --version
                 output version information and exit     
   .
   .
   .
   .

echo
--------------------


Imprime una frase o lo que sea que se escriba en la terminal:

.. code-block:: Bash 

   echo Hello world!
   
   ## Hello world!

pwd = print working directory
--------------------


Si necesitas saber en que directorio estas tranajando, este comando lo que hace es que imprime tu actual directorio 

.. code-block:: Bash 

   pwd
   
   ## /home/inb/paulinav

cd = change directory
--------------------


Este comando funciona para cambiar directorio. Cuando inicias sesión en tu computadora, lo más probable es que tu directorio sea el home y muy probable es que tengas que cambiar al directorio donde se encuentran tus datos. 

Mi directorio actual es:

.. code-block:: Bash 

   pwd
   ## /home/inb/paulinav
   

Cambio de directorio a donde esten mis datos:

.. code-block:: Bash 

   cd /misc/nyquist/paulinav/datos
   
   pwd
   
   ## /misc/nyquist/paulinav/datos
   

Para regresar directorios:

.. code-block:: Bash 

   cd ..
   
   ## /misc/nyquist/paulinav
   
   cd ../..
   
   ## /misc/nyquist
   
   cd ../../../
   
   ## /misc
   

ls = list
--------------------

Este comando va a enlistar los archivos que existen en tu actual directiorio. Supongamos que estamos en el home:

.. code-block:: Bash 

   ls
   
   ## Desktop
   ## Documents
   ## Downloads
   ## Music
   ## Videos
   
Pero tambien puedes utilizar ``ls`` para enlistar los archivos que existen en una ruta específica

.. code-block:: Bash 

   
   ls /misc/nyquist/paulinav/miniconda
   
   ## bin
   ## compiler_compat
   ## condabin
   ## envs
   ....ect
   

mkdir = make directory
--------------------


Ahora podemos crear uno o multiples nuevos directorios/carpetas con este comando:

.. code-block:: Bash 

   mkdir Mi_carpeta

o multiples:

.. code-block:: Bash 

   mkdir carpeta1 carpeta2 carpeta3

cp = copy
--------------------

Con este comando podemos hacer una copia de los archivos que queramos de un directorio a otro, por ejemplo:

.. code-block:: Bash 

   cp /misc/nyquist/paulinav/archivo.txt /misc/rhesus/paulinav/datos

mv = move
--------------------


este comando tiene dos funciones: mover el archivo de un lugar a otro o/y renombrar dicho archivo.
Para mover mi archivo de un directorio a otro:

.. code-block:: Bash 

   mv archivo.txt ~/Documentos
   
Para cambiarle el nombre:

.. code-block:: Bash 

   mv archivo.txt nuevo_archivo.txt
   
rm = remove
--------------------

Poderoso y peligroso. El comando ``rm`` es para eliminar archivos de forma **definitiva** ya que NO hay vuelta atrás una vez que lo ejecutas, así que aguas! Para usarlo solo necesitas darle el path del archivo:

.. code-block:: Bash 

   rm archivo.txt
o 

.. code-block:: Bash 

   rm /misc/nyquist/paulinav/archivo.txt

cat = concatenate 
--------------------


Este comando es muy útil y tiene varias funciones, entre las más relevantes es leer/imprimir, crear y unir archivos .txt, .sh y más. 

Para leer el contenido de un archivo .txt:

.. code-block:: Bash 

   cat archivo.txt

Para concatenar dos archivos:

.. code-block:: Bash 

   cat archivo1.txt archivo2.txt > nuevo_archivo.txt

Para crear un nuevo archivo:

.. code-block:: Bash 

   cat > archivo.txt

head
--------------------


Este comando imprime/lee las primeras líneas de un archivo y es muy util cuando estas explorando el contenido de ciertos archivos sin tener que ver todo el contenido usando ``cat``.
.. code-block:: Bash 

   head abecedario.txt
   
   ## A
   ## B
   ## C
   ## D
   
   
tail
--------------------

Mientras que ``tail`` lee las últimas lineas de un archivo:
.. code-block:: Bash 

   
   tail abecedario.txt
   
   ## W
   ## X
   ## Y
   ## Z

tree
--------------------


este comando despliega a los directorios con su estructura e información. Da una representación visual de las carpetas y sus archivos de manera muy eficaz. Ya que por ejemplo, ``ls`` si bien es efectivo, solo enlista los archivos de un solo path, mientras que ``tree`` despliega todos los directorios y sub directorios dentro del path.

.. code-block:: Bash 

   tree /home/paulinav
   
   # /home/paulinav
   # ├── Documents
   # │   ├── file1.txt
   # │   └── file2.txt
   # ├── Downloads
   # │   └── program1
   # └── Pictures
   #     └── image1.jpg

* = wildcard
--------------------


Uno de mis favoritos es el super asterisco ``*``, que es una manera altamente efectiva de filtrar, buscar y seleccionar archivos en un directorio. Aquí vamos a poner unos ejemplos.
Suponiendo que tenemos una serie de archivos en nuestro directorio:

.. code-block:: Bash 

   ls
   
   ## img.png
   ## img_hm.png
   ## img_rat.png
   ## img_b.png
   ## script_rat.sh
   ## script_hm.sh
   ## script_img.sh
   ## list_px.txt
   ## list_task.txt
   ## list_class.txt
   

Puedo seleccionar solamente todos aquellos con terminación ``.sh``:


.. code-block:: Bash 

   ls *.sh
   
   ## script_rat.sh
   ## script_hm.sh
   ## script_img.sh

O filtrar aquellos archivos que son relacionados a roedores:

.. code-block:: Bash 

   ls *rat*
   
   ## img_rat.png
   ## script_rat.sh

O seleccionar todos los archivos que empiecen con list:

.. code-block:: Bash 

   ls list*
   
   ## list_px.txt
   ## list_task.txt
   ## list_class.txt

& = ampersand
--------------------


Este es un indicativo al final de un comando que permite que se ejecute en el background mientras te permite seguir trabajando o escribiendo en la terminal. Un ejemplo donde es increiblemente útil es al abrir imágenes, por ejemplo:

.. code-block:: Bash 

   display imagen.png &












