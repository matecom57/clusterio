Fiji_stitching
==============


convertir ``.zvi`` y hacer mosaicos
--------------------


stitching directo en fiji (versión corta y chida)
--------------------

El plugin de stitching puede leer los ``.zvi`` directamente, jalando de los metadatos las coordenadas de la adquisición. Eso significa que incluso podemos 
olvidar si adquirimos el mosaico como **comb** o como **snake** (**wander**), y de todas maneras queda bien!

.. image:: stit01.png

.. image:: stit02.png


Y listones.



Conversión desde zvi (versión larga y tonta)
--------------------

El formato ``.zvi`` es propietario de Zeiss, pero en realidad es un tiff modificado con un poco de metadatos al principio. Afortunadamente, `bioformats <https://www.openmicroscopy.org/bio-formats/downloads/>`_ sabe leerlo y convertirlo a otros formatos más modernos y amigables.

Descargamos las "command line tools" de bioformats, y las descomprimimos a una nueva carpeta. Luego, esa carpeta la agregamos al PATH con un ``export``. Por ejemplo, en mi compu de la casa:


.. code:: Bash

   export PATH=/datos/syphon/lconcha/software/bftools:${PATH}
    
El comando que queremos es ``bfconvert``. Está padre, y nos ayuda a dividir la imagen como queramos. Yo la quiero frame por frame, pero en este caso se llama _series_. Por ejemplo, para convertir una imagen ``.zvi`` a muchos ``.png``, uno para cada frame uso:

.. code:: Bash

   bfconvert -channel 0 69B-30-Foxp2-40x.zvi tostitch/ch_%s_chan1.png
     
El ``-channel 0`` indica que solo quiero el primer canal (mi ejemplo es una imagen de dos canales; si hubiera querido el segundo canal hubiera indicado ``-channel 1``). 

La clave está en el ``%s`` en el output filename. Es un placeholder que cambiará en función de los archivos de salida. Al final, en la carpeta ``tostitch`` voy a tener muchos archivos .png diferenciados por su índice. Estúpidamente, bfconvert escribe números sin "padding", por lo que es necesario cambiarlos a tener una longitud similar para que alfabéticamente tengan sentido (que no vaya primero el 1 que el 10). Hay muchas maneras de hacerlo, pero haré uso de ``zeropad`` de fsl.

.. code:: Bash

   cd tostitch
   for f in *chan1.png
   do
     s=``echo $f | awk -F_ '{print $2}'``
     mv $f f_``zeropad $s 3``.png
   done

.. image:: stit03.png


:information_source: El formato png seguramente no es la mejor opción para lidiar con estas imágenes, debería estar usando tiff, pero para las pruebas basta el png.



stitching en Fiji
--------------------


Vamos a ``Plugings``, ``Stitching``, ``Grid/Collection Stitching``. Dependiendo si el mosaico se obtuvo con barrido _meander_ o _comb_, seleccionamos _grid snake by rows_ o _grid row by row_ respectivamente.


.. image:: stit04.png

Hay que decirle de qué tamaño es el mosaico (yo lo saqué por ensayo/error, pero pues hubiera sido mejor haberlo apuntado en una bitácora). Se le indica también dónde está la carpeta con los archivos y la nomenclatura de los mismos.

.. image:: stit05.png


Las ``iii`` en los _File names for tiles_ indican los índices de los archivos que cambiamos con el ``zeropad``.

Le damos ``OK`` y unos diez segundos después tenemos el resultado:

.. image:: stit06.png

Si nos equivocamos en lo de meander/comb o el número de cuadros, veremos algun resultado medio loco.

.. image:: stit06.png


Pendiente
--------------------

Hacer un script en Fiji que primero haga un _subtract background_ cuadro por cuadro y luego haga el stitching.
