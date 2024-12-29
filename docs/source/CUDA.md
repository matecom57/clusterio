# CUDA en Don Clusterio

CUDA es un sistema de procesamiento masivamente paralelo desarrollado por NVIDIA que se lleva a cabo en la tarjeta gráfica (GPU). Hace muchos procesos brutalmente más rápidos. No todo puede ser programado en CUDA, pero ciertas cosas lo aprovechan muchísimo, sobre todo las cosas de machine learning, y el programa eddy de fsl.

En Ubuntu 22.04 el default es instalar la versión 11 de CUDA, pero a fsl le gusta la versión 9.1. Para configurar la versión 9.1 usamos el siguiente comando:

```bash=
source /home/inb/lconcha/fmrilab_software/tools/inb_config_cuda9.sh
```

En realidad, lo único que hace ese script es revisar si CUDA 9.1 está instalado, y si sí, agregarlo al `LD_LIBRARY_PATH`.

Tienes duda si ya quedó? Usa el siguiente comando:

```bash=
inb_test_eddy_cuda.sh
```

:warning: No todas las PCs tienen GPU Nvidia, por lo que no todas las máquinas corren CUDA. Si vas a estar haciendo cosas en GPU, primero fíjate si puedes usarlo. 


:information_source: Update 25 de agosto 2022:
Existe una cola en SGE llamada `nvidia.q` que está configurada para ser usada a través de `fsl_sub` de fsl 6.0.2 o 6.0.5. Para mandar muchos jobs con programas que aprovechan CUDA, se puede usar:

    fsl_sub -q nvidia.q mi_script_que_usa_cuda.sh