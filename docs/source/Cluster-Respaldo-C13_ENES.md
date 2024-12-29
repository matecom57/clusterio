
**Lo que sigue aplica únicamente a las computadoras del laboratorio C13 y las de la Dra. García-Gomar (ENES-J).** Los usuarios de otros laboratorios son responsables de sus propios respaldos. Platiquen con su jefe/jefa sobre opciones.


# Respaldos del laboratorio C13 y ENES-J
Los respaldos de las **carpetas dentro de `/misc`** se realizan periodicamente, preferentemente en horarios que no coincidan con el uso del clúster.

:warning:  En el respaldo se exceptúan los datos  que se encuentran en la carpeta `tmp`, los archivos en la carpeta `Virtual Box` y los archivos contenidos en carpeta con nombre `nobackup`, `TMP*`, `tmp*`, `pruebas*`, `PRUEBAS*`, `Pruebas*` o `temporal*`. Tampoco se respalda `Dropbox`.

# Revisa tus respaldos!
Es importante que periódicamente revises que tus respaldos sí se estén haciendo. Localiza algún archivo que hayas generado la semana pasada, por ejemplo, y búscalo en los respaldos.

# Dónde están los respaldos
Para ver los respaldos, debes hacer `ssh` a la computadora `tesla` con tu nombre de usuario (no sabes ssh? pícale [aquí](./SSh). Una vez en `tesla`, encontrarás los respaldos de `/misc` en la carpeta `/bak.misc`. Dentro de ella, verás diferentes versiones temporales de los respaldos (los últimos 3 días, uno para la semana pasada, y uno para cada uno de los dos meses anteriores). Mira un ejemplo:

![image](https://github.com/user-attachments/assets/470d1e73-f53a-40cc-8895-949e1ba6c592)

:information_source: Los datos de cada PC se guardan en una carpeta que tiene su nombre. Por ejemplo, `/misc/mansfield` está en las carpetas `/bak.misc/mansfield-*`. Por lo tanto, no esperes encontrar (por ejemplo) datos que estaban en `/misc/carr` dentro de `/bak.misc/lauterbur-*`. Mira un ejemplo:

![image](https://github.com/user-attachments/assets/0ee93893-d1ea-4a76-b4af-3425680ae023)


:warning: La primera vez que navegas por las carpetas de `/bak.misc` habrá un rezago (se tarda), porque el sistema debe armar el árbol de directorios. Espera alrededor de un minuto antes de espantarte de que no funciona. Las siguientes llamadas a `ls` serán más ágiles.

:question: Qué pasa si no veo los respaldos? Lo más seguro es que el sistema está "desmontado". Esto sucederá después de apagones del cluster. No te desesperes. Avísale a Luis. Si estás segura/o que tu disco no se está respaldando, avísale a Luis, que seguramente olvidó agregarlo a la lista de discos a respaldar.

:hourglass_flowing_sand: Todo lo relacionado a los respaldos es lento, debes ser paciente. Recuerda que estamos respaldando cerca de 100 TB que deben comprimirse y de-duplicarse para caber en nuestros sistemas Synology. Esto se hace gracias al maravilloso [`borg`](https://www.borgbackup.org/), que de verdad que sí es maravilloso, pero no rápido.

# Datos antiguos

Para los datos que fueron procesados con mucha aterioridad y no estén actualmente en uso, es recomendable que se compriman y le avises a Luis para poder ser removidos de los discos que están activos en el clúster. Luis tiene discos viejos con datos de ex-alumnos. Si los necesitas, avísale.

