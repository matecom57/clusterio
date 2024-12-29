
rclone
======
  
  Luis Concha edited this page May 24, 2021 · 9 revisions

rclone te permite montar tu dropbox, google drive, amazon S3 y servicios similares como una carpeta local en linux!

Todas las máquinas del cluster ya tienen instalado rclone. Para verificarlo, escribe rclone en la terminal y debería mostrar las instrucciones y opciones. Si no lo hace, entonces avisa.

En la página de rclone encontrarás instrucciones sobre cómo montar una gran variedad de servicios. Todos son similares, así que aquí pondremos el ejemplo de cómo configurar Dropbox y cómo montarlo. Asumimos, por supuesto, que ya tienes cuenta en dropbox.
Configuración de rclone

    Configuramos rclone rclone config

    Seleccionamos New remote. Lo bautizaremos como dropbox (ojo, sensible a mayúsculas/minúsculas, yo decidí en minúsculas).

    Aparecerá la lista de servicios que rclone conoce. Selecciono el número que corresponde a dropbox.

    Nos pregunta por client_id, y lo dejamos en blanco (presionamos Enter), y lo mismo para client_secret. Cuando nos pregunte si queremos entrar a advanced config le decimos que n (o sea nel, en español).

    Cuando pregunta si queremos auto config le decimos que y.

    Se abrirá nuestro navegador de internet de manera mágica, con una pantalla como: snapshot

    Finalmente le decimos que y a cuando nos pregunte si todo está bien.

    Salimos de la configuración con q.

Montar Dropbox mediante rclone

    Designamos un lugar dónde montarlo y creamos el directorio, en caso necesario. En mi caso, montaré en /misc/mansfield/lconcha/nobackup/mnt_dropbox. Para facilitarme la vida, corro estos comandos:

dropbox_mount=/misc/mansfield/lconcha/nobackup/mnt_dropbox
mkdir $dropbox_mount

    ⚠️ La carpeta está adentro de una carpeta llamada nobackup. Ya sabes por qué, verdad? Si no sabes, consulta la entrada de Clúster ⚠️ Si alguna vez lconcha se encuentra una carpeta de éstas montada en algún lugar respaldable habrá consecuencias graves.

    Monto Dropbox en dropbox_mount:

rclone mount dropbox: $dropbox_mount

Se tarda unos segundos, pero ahora ya podemos ver los archivos adentro de esa carpeta, utilizando la terminal o cualquier gestor de archivos. Nota que el comando se queda colgado, eso quiere decir que está montado dropbox. Si cancelas ese comando, se desmonta dropbox.

    Desmontar es fácil. Simplemente tecleamos Ctrl+c en la terminal. Si alguna vez te da algún problema, la manera manual de desmontar es:

fusermount -u $dropbox_mount

  
