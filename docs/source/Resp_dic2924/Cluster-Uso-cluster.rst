
Clúster: Uso del clúster
------------------------

Luis Concha edited this page Nov 1, 2022 · 9 revisions

Como usuarios del clúster es necesario considerar varios factores para una buena ejecución de los trabajos que enviamos. La localización de los datos en el clúster los permisos y el estado de las colas de ejecución del clúster.

La manera más fácil de enviar un trabajo al cluster
---------------------------------------------------

Aunque la manera formal es utilizar ``qsub``, normalmente queremos que el comando que acabamos de escribir en la terminal se ejecute en el cluster, no en esta máquina. Para estos fines, nuestro amigo es ``fsl_sub``. Para usarlo, simplemente lo anteponemos a cualquier comando a ejecutar, con todo y los argumentos propios del comando a ejecutar. De manera general:

.. code-block:: bash

  $ fsl_sub <comando> [argumentos]

De esta forma, si queremos ejecutar el comando ``ls`` en el cluster, simplemente escribimos ``fsl_sub ls``, y si quisieramos argumetos, pondríamos, por ejemplo, ``fsl_sub ls -lart``.

fsl_sub tiene varias opciones que controlan en qué sistema de colas va a correr nuestro trabajo, la prioridad del mismo, e incluso nos permite utilizar un archivo lleno de jobs para mandar como un arreglo al cluster. Quizás la opción más util es la de nombrar a nuestro job, que por defecto simplemente será bautizado con un aburrido número. Si hemos enviado a procesar los datos de 50 sujetos al cluster, por ejemplo, nos gustaría saber qué sujetos siguen en ejecución. Para ésto, usamos:

.. code-block:: bash

  $ fsl_sub -N <nombreDelJob>

por ejemplo: ``fsl_sub -N suj331 recon-all -all -subjid 331``. El identificador suj331 aparecerá en la lista de jobs cuando usemos ``qstat``. Ojo, pues los nombres de jobs no pueden iniciar con un número.

Un ejemplo veloz para mandar a procesar a 5 sujetos en freesurfer:

.. code-block:: bash

  $ for suj in 301 302 303 304 305; do fsl_sub -N s${suj} recon-all -all -subjid $suj;done

en este ejemplo, cada job tiene la forma recon-all -all -subjid $suj, donde $suj toma el valor de 301 a 305. Estudia la sintaxis de fsl_sub y trata de entender cómo se le hizo.

Por qué fsl_sub?
----------------

``fsl_sub`` hace mucho más fácil enviar jobs al cluster. Simplemente se le antepone el comando a cualquier otro comando que hubiera corrido localmente. Si las carpetas input y output son visibles a través del cluster, el usuario no tiene nada más que hacer.

``fsl_sub`` es parte de las herramientas de fsl. Es un wrapper para el comando qsub, que es el que verdaderamente manda los jobs al cluster. Para más información del uso de fsl_sub consulta aquí.

Si quieres aprender a utilizar qsub de verdad, consulta acá. Ahí encontrarás el verdadero poder de qsub. Pero como dijo tío Ben: "Con gran poder viene gran responsabilidad".

Controlando multi-threaded jobs
-------------------------------

⚠️ Algunos comandos se paralelizan dentro de un CPU, usando una tecnología llamada multi-threading. Esto es **encima de la paralelización del cluster**. Los usuarios deben ser cuidadosos de al enviar jobs paralelizados al cluster.

ℹ️ Podemos usar ``fsl_sub -s smp,$nthreads miscript.sh``, donde -s significa ambiente paralelo, y sus opciones son smp que así está bautizado el ambiente configurado en Don Clusterio, y 4 que es un ejemplo de cuantos threads quiere uno usar. El número de threads es distinto en cada PC, pero la gran mayoría tiene 7; solo las más nuevas como nyquist o geminis tienen 15 

**Ejemplo**: ``fsl_sub -s smp,7 tckgen -nthreads 7 -algorithm iFOD2 -seed_image mask.mif csd.mif tractos.tck``. Nótese como -s smp,7 y -nthreads 7 coinciden. Así, la PC a la que le caiga usará 7 de sus 7 slots en este job en particular, y no le puede caer otro job similar de manera simultánea. En una PC con 15 slots, le pueden caer dos de estos jobs sin problemas, y no se pone lenta.

Una vez que enviaste tu job...
------------------------------

Para conocer el estado de las colas de ejecución se pueden usar los siguientes comandos:
  GNU nano 7.2                       www_rst.txt                                
.. code-block:: bash

  $ qstat -f

Permite ver los trabajos en una lista de hosts con los slot's en uso
locales/clúster/disponibles.

.. code-block:: bash

  $ qstat -u '*'

Permite ver todos los trabajos de todos los usuarios en ejecución

.. code-block:: bash

  $ qstat

Sólo muestra los trabajos del usuario que lo ejecuta

.. code-block:: bash

  $ qdel #

Permite borrar trabajos de la cola de ejecución, en este caso # se sustituye por el número del trabajo que se quiere eliminar

.. code-block:: bash

  $ qdel -u usuario

Borra todos los trabajos del usuario.

Si los trabajos no corren
-------------------------

Por favor revisa la página donde se explican los posibles errores

Cómo no usar el clúster
-----------------------

Por defecto, algunas herramientas como ``Feat`` o ``probtrack`` utilizan el cluster. A veces no lo quieres usar.

Para correr trabajos de fsl en la máquina de manera local sin entrar al clúster se puede usar los comandos:

``
unset FSLPARALLEL
unset SGE_ROOT
``

A partir de que se escribe esto en la terminal, el uso de programas se hará de forma local sin mandarlos al clúster. Sin embargo el equipo seguira formando parte del clúster. Cuando abras una nueva terminal se quitará este efecto mágico, y regresarás al default de sí usar el cluster.

Matlab en paralelo con SGE
--------------------------

No es posible paralelizar funciones de matlab al estilo matlab pool. Sin embargo, sí es posible paralelizar trabajos de matlab encapsulándolos en bash y mandándolos al cluster mediante SGE. Sigue estas instrucciones para aprender cómo.
