# Convertir con `brkraw`
###### tags: `tutorials` `Cluster` `bruker`

# Anaconda
Hay que instalar anaconda. Hay instrucciones [aquí](https://github.com/c13inb/c13inb.github.io/wiki/Anaconda) para instalarlo en el cluster.
Si no queremos instalar anaconda, podemos usar la instalación de `lconcha`. En ese caso, agregamos lo siguiente a `~/.bashrc`:

```bash=
echo "Use anaconda_on to turn on anaconda".
function anaconda_on() {
echo "[INFO] Initializing anaconda..."
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/misc/mansfield/lconcha/software/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/misc/mansfield/lconcha/software/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/misc/mansfield/lconcha/software/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/misc/mansfield/lconcha/software/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
echo "   anaconda is ready."
}
```

Ahora prendemos anaconda:

    anaconda_on
    
Y activamos el ambiente de brkraw

    conda activate /home/inb/lconcha/fmrilab_software/inb_anaconda3/envs/brkraw
    
Listo, brkraw está listo para usar.

# Convertir archivos
Podemos usar la forma gráfica de brkraw con el siguiente comando, y seguir los cuadros de diálogo que son bastante intuitivos para navegar a la carpeta que queremos convertir. 

    brkraw gui

![](https://i.imgur.com/V7KkJtG.png)
![](https://i.imgur.com/4t95zed.png)



Pero abajo vemos una forma más fácil para llegar directamente a los datos que nos importan.

## Encontrar archivos
Primero localizamos los archivos que queremos convertir. En 2023, estamos grabando en el disco `data02` de la consola del resonador, llamada `bruker7`. Este disco está accesible desde las PCs del cluster en `/misc/bruker7/data02`.

Por ejemplo, para encontrar un escaneo realizado el 9 de abril de 2023, podemos hacer:

    ls -d /misc/bruker7/data02/user/conchalab/20230409*
    
:spiral_note_pad: El `-d` es para solo mostrar los nombres de las carpetas, no subcarpetas.

Esto nos arroja:

```bash
lconcha@mansfield:~$ ls -d /misc/bruker7/data02/user/conchalab/20230409*
/misc/bruker7/data02/user/conchalab/20230409_111448_hluna_PTZirm2_rata1_hluna_PTZirm2_rata1_1_1
/misc/bruker7/data02/user/conchalab/20230409_112523_hluna_PTZirm2_rata1_2_hluna_PTZirm2_rata1_2_1_1
/misc/bruker7/data02/user/conchalab/20230409_123543_hluna_PTZirm2_rata3_hluna_PTZirm2_rata3_1_1
/misc/bruker7/data02/user/conchalab/20230409_134323_hluna_PTZirm2_rata4_hluna_PTZirm2_rata4_1_1
/misc/bruker7/data02/user/conchalab/20230409_144815_hluna_PTZirm2_rata5_hluna_PTZirm2_rata5_1_1
/misc/bruker7/data02/user/conchalab/20230409_155337_hluna_PTZirm2_rata6_hluna_PTZirm2_rata6_1_1
/misc/bruker7/data02/user/conchalab/20230409_165719_hluna_PTZirm2_rata5_2_hluna_PTZirm2_rata5_2_1_1

```

Con eso vemos todas las ratas escaneadas en tal fecha. Decidimos que queremos convertir, por ejemplo, la `rata4` y queremos colocar el archivo resultante en la carpeta `/misc/mansfield/lconcha/TMP`, entonces:

## Convertir
Como ya sabemos dónde está la carpeta, se la damos de una vez a brkraw:

    brkraw gui -i /misc/bruker7/data02/user/conchalab/20230409_134323_hluna_PTZirm2_rata4_hluna_PTZirm2_rata4_1_1

Esto abre directamente la carpeta del animal que queremos. A la izquierda vemos la lista de escaneos. En el panel de en medio vemos las imágenes, y podemos usar los _sliders_ para cambiar rebanada/volumen. A la derecha vemos información relevante al escaneo. 

![](https://i.imgur.com/YL4bWR7.png)


:one: El botón *SetOutput* nos permite decir en dónde queremos colocar el archivo resultante. Al darle clic, navegamos a la carpeta donde queremos aventar nuestros archivos NIFTI resultantes (en este ejemplo, en `/misc/mansfield/lconcha/TMP`)

:two: Ahora, seleccionamos la imagen que queremos convertir, y simplemente presionamos *Convert* 

![](https://i.imgur.com/IQxbAZm.png)

Ya con calma, vamos a la carpeta donde se guardó nuestro archivo, y cambiamos el nombre del chorizo que es actualmente a algo que sea más digerible (p.ej. `rata04_PTZ.nii.gz`).


## Pura línea de comandos
Ya vimos cómo hacer la conversión mediante la manera gráfica. Pero como soy flojo y odio los clics, prefiero hacer todo desde la línea de comandos.

Para ver la lista de los escaneos de la rata:

    brkraw  info /misc/bruker7/data02/user/conchalab/20230409_134323_hluna_PTZirm2_rata4_hluna_PTZirm2_rata4_1_1/
    
![](https://i.imgur.com/AgnDpdG.png)

La flecha roja apunta a la que quiero, que es el escaneo `02`

Y de una vez le vamos a decir cómo se va a llamar el archivo, para no tener que andarlo cambiando después. Entonces:

    brkraw tonii -o /misc/mansfield/lconcha/TMP/rata04_PTZ_T1 -s 2  /misc/bruker7/data02/user/conchalab/20230409_134323_hluna_PTZirm2_rata4_hluna_PTZirm2_rata4_1_1/

`tonii` está avisando que vamos a convertir, no a ver. `-o` está diciendo cómo se llamará el output (por eso sigue toda una ruta con el nombre del archivo resultante); `-s` está diciendo qué escaneo queremos (por eso sigue un `2`), y lo último que le dimos es la ruta del origen de los archivos del resonador.

![](https://i.imgur.com/9YesNSJ.png)