# Mover `home` del servidor a una computadora cliente


Ahora que estamos teniendo problemas con el servidor, `tesla`, se ha hecho muy lenta la lectura/escritura de datos al `home` de los usuarios. Esto sobre todo se nota al abrir programas como libreoffice, gedit, etc, que tienen que leer preferencias grabadas en `home`. 

Mientras encontramos una solución definitiva, hice un script que mueve todas las carpetas de configuración desde `tesla:/home/inb/USER` a alguna de las computadoras cliente. Lo lógico es moverlo a la máquina donde nos sentamos. Por ejemplo, Ale lo pondría en `hahn`, y Luis lo podría en `mansfield`. 

En el siguiente ejemplo, `USER2` ha movido su home desde `tesla` hacia `hahn`. 
![](https://i.imgur.com/jdskemd.jpg)

Ojo, que solo se copian las carpetas de configuración (las que están ocultas en `home`, y que inician con un punto `.`); los archivos *reales* que uno tenga en su home se quedan en el servidor. Después de copiadas las carpetas de configuración, se hacen links simbólicos para apuntar a su nueva localización en la computadora cliente (línea punteada).

## Mover carpetas (de ida)
Estando físicamente en la máquina que queremos usar, o conectado mediante ssh, usamos el comando `inb_create_home_links.sh`
```
lconcha@mansfield:~$ inb_create_home_links.sh 

inb_create_home_links.sh <machine> [-options]

 Copia los archivos de /home/inb/lconcha a una carpeta en /misc:
    /misc/[machine]/lconcha/nobackup/home_links


 Options:

 -h, -help : Imprime esta ayuda.
 -reverse  : Revierte los efectos de este script
             (regresa los archivos a /home/inb/lconcha)
             PRECAUCION: Importante especificar la misma [machine] que cuando se corrio de ida este script.

 
LU15 (0n(H4
INB, UNAM
Septiembre 2020
lconcha@unam.mx

```
Por favor revisa que la máquina donde vas a copiar tenga suficiente espacio en `/misc/machine`, donde `machine` es algo como `hahn`, `carr`, etc.


## Revertir cambios (de vuelta)
Usamos el mismo script, pero con el switch `-reverse`.


Como todas las cosas de andar copiando y moviendo archivos, vale la pena hacer un respaldo previamente.

