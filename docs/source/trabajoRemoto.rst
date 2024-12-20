
trabajoRemoto

git-terbug edited this page Apr 22, 2024 · 5 revisions

Trabajando remotamente
======================

A veces, estando en tu casa, en el café, o en cualquier parte del mundo, necesitarás tus datos que están en las computadoras del cluster. Otras ocasiones querrás dejar corriendo trabajos en el cluster desde tu sofá. Otras, querrás revisar el resultado de tus scripts en tu laptop. O quizás los de la entrada del Campus no te dejaron entrar en vacaciones porque estaban de mal humor. En cualquier caso, tienes varias opciones para acceder al cluster desde cualquier parte del mundo.

    ⚠️ Solo UNA computadora de todo el cluster es accesible desde fuera del INB, y es ``penfield.inb.unam.mx``. Una vez que llegues a penfield podrás brincarte a cualquier otra computadora del cluster, y ver el contendido de tu home y de ``/misc``.

Quiero un artículo que no puedo acceder en casa
-----------------------------------------------

Lo mejor es hacer un túnel ssh al laboratorio, y usar tu navegador local para ir al artículo Primero hacemos el túnel:

.. code-block:: bash

    $ ssh -ND 8080 USER@penfield.inb.unam.mx

Te pedirá tu password de las computadoras del laboratorio. Luego vamos a otra terminal y abrimos un navegador web:

.. code-block:: bash

    $ chromium-browser --proxy-server="socks5://localhost:8080"

Esto se puede hacer igualito usando google-chrome. Y sé que se puede hacer con firefox, usando la extensión foxyproxy. Búscala y si aprendes a hacerlo, edita esta página.

Para firefox, podemos utilizar la extensión multi-account-containers, con la ventaja de que podemos crear diferentes entornos para cada pestaña. Abrimos la extensión y hacemos click en administrar contenedores; creamos uno nuevo ex-profeso para todas nuestras necesidades remotas, personalizamos nuestro contenedor al gusto y en "configuración avanzada del proxy" escribimos "socks://localhost:8080". Le damos aplicar y ¡listo! Más info

Quiero acceder gráficamente, con un entorno de escritorio
---------------------------------------------------------

Excelente, es una experiencia muy agradable tener una "computadora dentro de una computadora". Por favor sigue el tutorial de x2go.

Quiero una terminal nada más
----------------------------

Minimalista, eh? Bien, utiliza ssh.

Yo solo quiero copiar mis archivos desde el cluster a mi laptop
---------------------------------------------------------------

Para ésto puedes usar dos opciones:

scp
---

``scp`` significa secure copy, y su funcionamiento es análogo al clásico cp (copy, ver manual). El manual completo de scp está acá, pero es muy fácil: su sintaxis es scp ORIGEN DESTINO, pero en este caso, tanto ORIGEN como DESTINO son una ruta completa ya sea local, o remota. En el caso de carpetas remotas, se especifica el usuario que accede a una máquina, y la ruta del o los archivos a copiar. Por ejemplo, desde una laptop fuera del INB:

.. code-block:: bash

    $ scp lconcha@penfield.inb.unam.mx:/misc/mansfield/lconcha/misResultados/final.txt /home/lconcha/Desktop/

En este ejemplo, estoy copiando (usuario ``lconcha``) el archivo ``final.txt``, que está en una ruta dentro de ``/misc``, que es visible por la computadora ``penfield.inb.unam.mx``, y lo voy a poner en mi laptop, en el ``Desktop``. Si hubiera querido copiar toda la carpeta, igual que con ``cp``, debería utilizar el switch ``-r`` (recursive).

rsync
-----

La principal desventaja de ``scp`` es que le gusta copiar todo, y si algo falla, tienes que volver a empezar. Esto es muy frustrante con carpetas grandes. Pero la herramienta rsync te permite continuar una descarga en donde te quedaste. Su uso básico es igual a scp, mediante rsync ORIGEN DESTINO. Es habitual utilizar los switches -avzh (archivo, verbose, comprimido y modo humano, respectivamente). Tomando el ejemplo anterior:

.. code-block:: bash

    $ rsync -avzh lconcha@penfield.inb.unam.mx:/misc/mansfield/lconcha/misResultados/final.txt /home/lconcha/Desktop/

Hay un tutorial muy bueno de rsync aquí.

Un truco muy bonito es generar un alias con todas las mejores opciones de rsync en un comando facilito de usar. Por ejemplo podemos hacer el alias del comando scpresume, para llamar a rsync con mil opciones, y usarlo cómodamente como si fuera un scp:

.. code-block:: bash

    $ alias scpresume='rsync -avz --partial --progress --rsh=ssh'
scpresume lconcha@penfield.inb.unam.mx:/misc/mansfield/lconcha/misResultados /home/lconcha/Desktop/

Este último ejemplo copiaría toda la carpeta misResultados dentro de Desktop en la laptop, y si algo fallara, lo puedo volver a correr, y continuará donde se quedó.

Me gustaría ver la carpeta remota como si fuera local
-----------------------------------------------------

Elegante! Es una manera muy cómoda para, por ejemplo, utilizar mrview en tu laptop para ver un archivo que está en el cluster, sin tener que copiarlo! (Considera que cada vez que lo vas a visualizar, el archivo viajará por internet, por lo que archivos demasiado grandes sí tardarán en abrir).

Primero, en tu laptop debes instalar ``sshfs`` (ssh file system). En ubuntu es muy fácil:

.. code-block:: bash

    $ sudo apt install sshfs

Si no estás en ubuntu, chécate este tutorial para otras instalaciones.

Ahora vamos a montar la ruta remota en una carpeta local. La carpeta local debe existir y debemos tener permisos de escritura. Por ejemplo, voy a crear la carpeta local dentro de mi ``home`` de mi laptop, y voy a montar ``/misc`` ahí:


mkdir /home/lconcha/misc
sshfs lconcha@penfield.inb.unam.mx:/misc /home/lconcha/misc

Se ve en la sintaxis que funciona como los ejemplos anteriores, donde mencionamos el usuario, la computadora y la ruta (remotos) que queremos montar (local). Como sshfs depende de ssh, me pedirá mi password del cluster. Ahora, si yo hago ls /home/lconcha/misc, veré las mismas carpetas que si yo hiciera ls /misc en una computadora del cluster. Incluso podría ver una imagen, tipo mrview /home/lconcha/misc/mansfield/imagen.mif.
