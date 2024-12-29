# Preguntas Frecuentes

¿Por qué no abre Firefox?
:     Si bien puede haber  algún problema con la aplicación, en la mayoría de los casos el problema se debe a que una sesión de Firefox quedó abierta en alguna otra máquina. Firefox no permite dos sesiónes de usuario al mismo tiempo por el mismo usuario en diferentes máquinas. Esto se puede solucionar abriendo la máquina dónde está la sesión de Firefox y cerrarlo. Sin embargo si la máquina en cuestión está ocupada, es posible hacer una sesión [ssh](./SSh) a la máquina en cuestion y ya ahí [matar el proceso](./Bash:-Kill), de preferencia a través de la terminal.

Cuándo cambio de usuario la máquina no responde y la pantalla se pone negra
:     Esto se debe a que hubo algún error en la carga del sistema de gráficos en el equipo. Puede deberse a un fallo de la tarjeta de video, que puede agravarse por programas que quedan abiertos por alguno de los usuarios. Es recomendable cerrar los programas en ejecución y de ser posible salir de la sesión. Si este problema se presenta, lo mejor es llamar al administrador del sistema para que restablezca el sistema.


¿Por qué cuándo paso mis PAR/REC del Philips a Penfield no se ven los archivos NIfTI?
:     Es dificil de saber la causa de esto, en ocaciones puede ser por errores en el clúster mientras se copiaban los datos, lo cuáles pueden llegar incompletos. Hay que volver a pasarlos desde la base de datos del resonador.
NO debes borrar los datos de la base de datos del Philips hasta que se este seguro que se tienen las imágenes íntegras.

# Alertas

¿Cómo lograr que médicos clínicos vean la IRM?
:     Para compartir las imágenes de IRM con médicos clínicos los datos tienen que extraerse directamente de la máquina de dónde se hayan exportado en una memoria externa, ya que la mayoría de los programas médicos usados en clínica no pueden leer el disco grabado en VIRTUAL. Los archivos pueden ser enviados de forma comprimida (.zip) para mayor velocidad y eficiencia.


# Trucos de Luis Concha ##
Algunos trucos de cosas truculentas, y otras muy bobas pero que me tardé en entender cómo hacerlas.

Lo que hago más frecuentemente es un for loop, que directamente en la terminal debe usar punto y coma en sustitución de un script formal en dónde se hace una nueva línea. Por ejemplo:

``` bash
for sujeto in 301 302 303
do
  echo "trabajando en sujeto $sujeto"; done
```
en la terminal quedaría:

```bash
for sujeto in 301 302 303; do echo "trabajando en sujeto $sujeto"; done
```
Nótese la ausencia de punto y coma entre do y echo.

En caso de tener organizados a los sujetos cada uno con una carpeta, y con identiricadores claros, como en el caso de freesurfer, es muy fácil hacer algo repetitivo:

```bash
for sujeto in 3??; do recon-all -all -subjid $sujeto;done
```

## Poner resultados FEAT en Freesurfer ##
Una manera muy fácil se explica [aquí](./FSL:-project-to-fsaverage).

Una alternativa más viejita y complicada está [acá](./FEAT2FS).
