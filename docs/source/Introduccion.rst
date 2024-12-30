Introducción
============

**Don Clusterio** es una red de computadoras de escritorio identificadas por su **nombre** y su correspondiente número identificador ``IP``.
Todas estas maquinas tienen instalado el Sistema Operativo Linux UBUNTU V22, y el software necesario para que todas las maquinas trabajen 
de manera distribuida y paralela. Para que se realice el trabajo conjunto de Don Clusterio tiene los Softwares: NIS, NFS y SGE.

Para utilizar los recursos de Don Clusterio, cada usuario debe tener una cuenta en ```Rocket-Chat`` y tener una ``cuenta de usuario```en el Sistema UBUNTU.

Al crear una cuenta de usuario, se crean dos folder, uno de manera automatica llamado ``HOME`` (path absoluto: ``/home/<usuario>`` donde
``<usuario>`` es el usuario creado, en este folder no ocupar mas de ``30 GB``, el otro folder es ```/mis/<maquina>/<usuario>`` donde ``<maquina>``
es el nombre de la maquina de **Don Clusterio**.

**Por ejemplo:**

.. code-block:: Bash

   /home/santosg
   /misc/tournoux/santosg

La mayoria de la utileria para manejar, almacenar y analizar **imagenes de resonancia magnetica** se maneja en ``modo terinal```. Para entrar en 
mod terminal uno debe presional al mismo tiempo las teclas: ``CTR-ALT-T`` al estar en modo y aparecera la siguiuente ventana:

.. code-block:: Bash

   (base) leopoldogonzalez@Leopoldos-MacBook-Pro source % ssh santosg@penfield.inb.unam.mx
   santosg@penfield.inb.unam.mx's password: 
   Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 6.8.0-40-generic x86_64)

   * Documentation:  https://help.ubuntu.com
   * Management:     https://landscape.canonical.com
   * Support:        https://ubuntu.com/pro

   Expanded Security Maintenance for Applications is not enabled.

   56 updates can be applied immediately.
   To see these additional updates run: apt list --upgradable

   48 additional security updates can be applied with ESM Apps.
   Learn more about enabling ESM Apps service at https://ubuntu.com/esm

   New release '24.04.1 LTS' available.
   Run 'do-release-upgrade' to upgrade to it.

   *** System restart required ***
   Last login: Sun Dec 29 14:42:40 2024 from 172.24.142.254
   ╔╦╗┌─┐┌┐┌  ╔═╗┬  ┬ ┬┌─┐┌┬┐┌─┐┬─┐┬┌─┐
   ║║│ ││││  ║  │  │ │└─┐ │ ├┤ ├┬┘││ │
   ═╩╝└─┘┘└┘  ╚═╝┴─┘└─┘└─┘ ┴ └─┘┴└─┴└─┘
   ====== INB ============= UNAM ======
   Hola santosg. Bienvenido a penfield.
   --------------------------------------------------------------- 
   Usa módulos para ajustar tu ambiente: 
      'module avail' - Muestra los módulos disponibles. 
      'module load <module>' - Carga el módulo para esta sesión. 
   Más información en https://github.com/c13inb/c13inb.github.io/wiki/Modules  
   --------------------------------------------------------------- 
   Python: Instala tu propia Anaconda o miniconda. Instrucciones: 
          https://github.com/c13inb/c13inb.github.io/wiki/Anaconda 
   --------------------------------------------------------------- 
   Visita la wiki:
   https://github.com/c13inb/c13inb.github.io/wiki 

   RESPALDOS: SOLO PCS DEL C13 SE RESPALDAN AUTOMATICAMENTE 
              Todos los demás laboratorios deben tener su propia estrategia de respaldo. 

   Utiliza el canal #don_clusterio en la Red-Lanirem 

   (base) santosg@penfield:~$ 


xx

   



