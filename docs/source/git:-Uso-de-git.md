### Instalación y configuración de GIT

Se necesita instalar __git__ y __git-core__ para que funcione como __servidor__, si solo se requiere clonar un repositorio solo instalamos git:

    sudo apt-get  install git-core git  


### Clonar un repositorio

Para obtener una copia de un repositorio se usa la instrucción

    git clone usuario@penfield:/datos/penfield/git/proyecto.git

Con esta opción obtenemos una copia del repositorio maestro de el proyecto. Si el repositorio es nuevo no descargara nada.


### Crear un Repositorio ###

En el servidor se crea una carpeta que funcionara como repositorio, este debe ser configurado sin directorio de trabajo _(opción --bare)_, y con permiso de lectura escritura y ejecución para el grupo tanto en el sistema de archivos como en la configuración de __git__ _(opción --shared)_. Primero creamos la carpeta, determinamos los usuarios, grupos y permisos pertinentes para la carpeta y nos cambiamos a ella:


    mkdir -p /datos/penfield/git/proyecto.git
    chown usuario:fmriuser /datos/penfield/git/proyecto.git
    chmod g+wr /datos/penfield/git/proyecto.git
    cd /datos/penfield/git/proyecto.git

Dentro de la carpeta iniciamos el repositorio __git__:


    git init --bare --shared 


Hay que estar seguros de que el grupo de trabajo contiene a los usuarios que
podrán hacer modificaciones y que el repositorio (proyecto.git) esta a nombre
del grupo de trabajo.


A partir de este momento este repositorio se puede utilizar, aunque de momento no tiene nada dentro. Puede clonarse en el servidor local para comenzar a trabajar.

        git clone usuario@penfield:/datos/penfield/git/proyecto.git


Al clonarse, la instrucción creara una carpeta con el nombre del __proyecto__ en la carpeta donde se ejecuta este comando. 
En esta carpeta podemos agregar algún archivo para realizar el primer commit. Por ejemplo el archivo .gitignore para que git ignore ciertos archivos.

    echo "*.swp" > .gitignore
  
> __Nota:__    
> Esto es solo necesario si no se tienen archivos con los cuales hacer un commit o es la primera vez que se usa. Este comando por segunda vez podría eliminar modificaciónes posteriores sobre __.gitignore__

Ya con los archivos se realiza el commit

    git add .
    git commit -m 'Commit inicial'
    git push origin master

> __Nota:__
> En la primera vez se necesita usar master, para que se agregue la branch, de lo contrario no funcionara.


Ya clonado, los repositorios se agregan automaticamente, Sin embargo si es necesario se puede agrega un repositorio remoto:

    git remote add origin usuario@penfield:/datos/penfield/git/proyecto.git

Esta es la instrucción para agregar un repositorio que se accede por [ssh](?id=ssh), por lo que seguramente nos pedira un password. A menos que hayamos configurado una ssh-key para el servidor. La instrucción para agregar otro tipo de repositorio se encuentra en la [documentación](http://git-scm.com/book/en/Git-Basics-Getting-a-Git-Repository) de git.    



### Branchs ###


Para crear una Branch


    git checkout  mybranch


Para crearla y pasarse a ella 


    git checkout -b mybranch


Regresar a la branch principal 

    git checkout master


Para unir el trabajo de la rama nueva con la rama vieja, primero nos pasamos a
la rama maestra


    git checkout master


Y luego hacemos el merge de nuestra branch


    git merge mybranch


Cuando se hace un merge se suele dar prioridad al merge que primero se hace.
Además si el master de donde parte nuestra branch ha sido cambiado de alguna
forma, por ejemplo un merge de otra rama, git fusiona los diferentes snapshots.
Esto solo  cambia cuando al hacer el merge, la rama y el master cambian el
mismo archivo-línea. En este punto merge pide asistencia para definir a cual
darle prioridad.   

En el caso de querer borrar una branch se usa el comando:


    git branch -d mybranch


Para ver el último commit de cada branch:

    git branch -v

Para subir una rama en la que querramos colaborar, es necesario que exista el
repositorio y se usa el siguiente comando:

    git push origin myotherbranch

Es posible, si queremos que el nombre en el servidor remoto sea distinto,
determinar otro nombre para la branch, usando el comando:


    git push origin myotherbranch:otronombredelabranch


En la siguiente ocasión en la que un colaborador obtenga el repositorio
aparecera la rama que se subio al mismo. Pero esta rama sera solo un apuntador
a la posición origin/mybranch que no esta disponible para edición. Para poder
acceder a esta rama y poder hacer modificaciones se usa el comando:


    git checkout -b myotherbranch origin/myotherbranch


Si se quiere hacer automáticamente el fetch y el push es necesario activar el
tracking para dicha branch. Mediante:


    git checkout --track origin/serverfix


En versiones anteriores se usaba el siguiente comando:


    git checkout -b myotherbranch origin/myotherbranch


Si por ejemplo la rama en la que estamos trabajando deja de ser funcional y
necesitamos  borrar la rama remota se borra con el siguiente comando:


    git push origin :mybranch


Este comando funciona considerando el constructo de la función git push
_remotename_ __localbranch__: *remotebranch* y aquí nos deshacemos de la parte del
localbranch y le decimos que con eso forme el remotebranch. Al estar el local
vacío, sustituye la branch remota por nada.


### Uso cotidiano ###


En el uso cotidiano los pasos a seguir para registrar los cambios son:


    git add .
 
ó


    git add *


ó


    git add nombredearchivo


Esto agrega los archivos para que se anexen al siguiente commit. Después de
esto se hace el commit para consolidar los archivos y los cambios en la
historia de la carpeta:


    git commit


Esto abre un editor de texto (que se puede cambiar) que pide un mensaje que
pueda describir el commit. Si no se proporciona el mensaje no se realiza el
commit. Estos pasos se pueden resumir en el siguiente comando:


    git commit -a -m ‘My commit’




Donde: 

-a
: agrega todos los archivos con cambios al commit, pero no agrega
archivos nuevos  

-m
: permite escribir el mensaje para el commit entre comillas.  


Otro punto importante es observar el estado de los archivos en la carpeta, esto
se realiza mediante:


    git status


Incluso si se tienen los colores activados, este comando muestra en rojo los
archivos que no han sido incluidos en el commit y en verde los que sí se han
incluido. 


Para borrar archivos, se pueden borrar normalmente con rm nombre de archivo,
sin embargo cuando se haga el commit tendremos que borrar también con:


    git rm nombredearchivo


Siendo buena práctica desde el principio usar este comando en la carpeta con
git, ya que borra el archivo e informa de esto a git. O usar durante el commit
la opción -a, sin embargo en ocasiones si necesitamos más control es mejor
hacerlo paso a paso.


### Buenas prácticas
Cada desarrollador o equipo de desarrollo puede hacer uso de Git de la forma que le parezca conveniente: Sin embargo una buena práctica es la siguiente

Se deben utilizar 4 tipos de ramas Master, Development, Features, y Hotfix:

**Master**
Es la rama principal: Contiene el repositorio que se encuentra publicado en producción, por lo que debe estar siempre estable:

**Development**
Es una rama sacada de master: Es la rama de integración, todas las nuevas funcionalidades se deben integrar en esta rama: Luego que se realice la integración y se corrijan los errores (en caso de haber alguno), es decir que la rama se encuentre estable, se puede hacer un merge de development sobre la rama master.

**Features**
Cada nueva funcionalidad se debe realizar en una rama nueva, específica para esa funcionalidad: Estas se deben sacar de development: Una vez que la funcionalidad esté pronta, se hace un merge de la rama sobre development, donde se integrará con las demás funcionalidades. 

**Hotfix**
Son bugs que surgen en producción, por lo que se deben arreglar y publicar de forma urgente: Es por ello, que son ramas sacadas de master: Una vez corregido el error, se debe hacer un merge de la rama sobre master. 
Al final, para que no quede desactualizada, se debe realizar el merge de master sobre development.

