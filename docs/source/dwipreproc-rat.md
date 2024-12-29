# Preproceso de 2D-EPI DWI con eddy

Analizar datos de difusión puede ser bastante sencillo, pero para lograrlo se requiere que los datos estén en buenas condiciones. Estos pasos buscan corregir algunos artefactos de adquisición y limpiar los datos lo más posible, de manera que la estimación de parámetros de difusión sea adecuada. El preprocesamiento es habitualmente más tardado y latoso que el procesamiento mismo, y cada paso es toda un tópico en constante investigación y desarrollo. Aquí se describen los pasos que seguimos habitualmente (julio 2021). El ejercicio está orientado a datos de roedor adquiridos con nuestro Bruker de 7 T, pero los conceptos son los mismos para datos de humanos. Estos pasos pueden usarse en su mayoría sin modificaciones con adquisiciones EPI3D.

:information_source: El comando `dwifslpreproc` de mrtrix encapsula la mayoría de estos pasos. Sin embargo, se sugiere que toda persona involucrada en difusión lea este ejercicio y arme su propio pipeline de preprocesamiento. Esto es por dos razones: Primero, las cajas negras nunca son buenas cuando uno se dedica a aprender cosas, y por éso estamos en el ámbito académico ¿no?. Segundo, los defaults de `dwifslpreproc` están afinados para datos de humanos, y cuando lidiamos con DWIs de roedores, la cosa cambia bastante.

:information_source: Otra fuente de información muy útil para aprender sobre preprocesamiento de DWI es [Andy's brain book](https://andysbrainbook.readthedocs.io/en/latest/MRtrix/MRtrix_Course/MRtrix_04_Preprocessing.html). Aunque los datos ahí preprocesados son de humanos, muchos de los conceptos son similares con lo que hacemos con datos de ratas. De paso date una vuelta por el resto de esa página, que está fenomenal.

:tipping_hand_person: Estos pasos han sido encapsulados en el script `inb_dwi_bruker_preproc.sh` disponible el 24 de agosto de 2021 en Don Clusterio. Invoca el comando sin argumentos para aprender su uso. El script tiene la ventaja que además de hacer todo ésto, utiliza `eddy_quad` para hacer un reporte de control de calidad. Como bonus, se generan imágenes `png` para una rápida visualización de mapas RGB antes y después de pre-procesar los datos. Ojo, que aunque existe el script, se recomienda leer esta entrada para que sepas qué hace esa caja negra. El script está pensado en datos EPI-2D de rata, pero es probable que funcione en ratón, y con datos 3D-EPI. Para datos de humanos sería más conveniente usar `dwifslpreproc`.

## Convertir de bruker a nifti
Hay dos maneras, con las herramientas de mrtrix y scripts del laboratorio, o con brkraw. 

Para este ejercicio, voy a usar unos datos adquiridos por Alejandra Garay e Hiram Luna que están guardados en una ruta de `/misc`  (que **se pueden bajar desde [este link](https://drive.google.com/file/d/1zsYkIuYDUeZZwslLpbwsX156dPn3T8Ci/view?usp=sharing)**), y sobre los que yo sé _a priori_ que el escaneo número `4` contiene los datos de difusión. Para facilitar el ejercicio, los convertiré en variables:

```bash=
BRUKERFOLDER=/misc/hahn2/difusion_aprendizaje/20210712_092738_INB_C13_hluna_irm1_rata277_1_1
SCANNUMBER=4
```


:information_source: Recordemos que si el B0map (map shim) se hace justo antes de la adquisición de difusión, entonces habrá dos reconstrucciones del scan `4`. La primer reconstrucción será siempre la de las imágenes de difusión, y la segunda es el B0map. Además, en el set de difusiones, podremos encontrar como reconstrucción aparte los mapas cuantitativos de DTI calculados por Paravision, los cuales podemos ignorar.

:information_desk_person: Más información sobre cómo convertir de bruker a nifti por [acá](https://github.com/c13inb/c13inb.github.io/wiki/Resonadores:Bruker).


:dizzy_face: Los archivos `.mif` contienen la información de los gradientes dentro de un encabezado en el archivo mismo. Los nifti no pueden hacer ésto, por lo que se requieren dos archivos más que siempre le acompañan, los bvalues y los bvectors. En lo personal odio un poquito tener que andar llamando a esos otros dos archivos cada que quiero hacer algo, así que prefiero usar archivos `mif`, pero nada impide que hagas todo tu procesamiento con archivos nifti.




### Convertir con brkraw
Primero que nada, debemos tener configurada anaconda, lo que logramos en el cluster con un simple `inb_anaconda_on`. [Acá hay más información](https://github.com/c13inb/c13inb.github.io/wiki/Anaconda) sobre anaconda en don clusterio.
Ahora iniciamos el ambiente `brkraw` que instaló lconcha.
```bash=
conda activate brkraw
```
Podemos usar brkraw mediante un ambiente gráfico mediante el comando `brkraw gui`, que es bastante intuitivo. Si así prefieres, adelante. Yo soy fan de la terminal, así que aquí va cómo le hago.

```bash=
brkraw tonii  -o r277 -s $SCANNUMBER $BRUKERFOLDER 
```
Checamos con `mrinfo` y notamos que el archivo generado tiene 202 volúmenes, como esperábamos. Además se generaron los archivos `.bvec` y `.bval` correspondientes.

Solo resta convertir a `mif`:
```bash=
mrconvert -bvalue_scaling false -fslgrad r277-4-1.bvec r277-4-1.bval r277-4-1.nii.gz dwi.mif
```

### Convertir vía mrtrix
Esta es la vía clásica y que usamos en el C13 mucho tiempo. Sin embargo, la opción mediante brkraw es más robusta y regresa archivos `bvecs` sin escalamiento. **Se sugiere usar la opción brkraw**.
```bash=
inb_bruker_recursive_convert_mih.sh $BRUKERFOLDER r277
```
Esto generará los archivos `.mih` de toda la adquisición. Podemos revisar cada uno con `mrview` y asegurarnos que `r277_004_DWI_3shell_E4.mih` es la adquisición que queremos. Veamos su header:
```bash=
mrinfo r277_004_DWI_3shell_E4.mih
```
```
mrinfo: [WARNING] transform matrix contains invalid entries - resetting to sane defaults
************************************************
Image name:          "r277_004_DWI_3shell_E4.mih"
************************************************
  Dimensions:        134 x 120 x 25 x 202
  Voxel size:        0.149254 x 0.15 x 1.25 x ?
  Data strides:      [ 1 2 3 4 ]
  Format:            MRtrix
  Data type:         signed 16 bit integer (little endian)
  Intensity scaling: offset = 0, multiplier = 1
  Transform:                    1           0           0      -9.925
                                0           1           0      -8.925
                                0           0           1         -15
  dw_scheme:         0,0,-0.0,21.0108281961807
  [202 entries]      0,0,-0.0,21.0108281961807
                     ...
                     -0.530627197518155,-0.218121955383739,-0.0463487605318663,1255.66462041204
                     -0.822044119613011,-0.337913080257368,-0.0718031910629095,3002.6031225321
```
Tiene 202 volúmenes y contiene la tabla de gradientes de difusión. Muy bien. 
Solo nos falta convertir a `mif` (recordemos que `mih` es solo un header, no los datos).
```bash=
mrconvert -bvalue_scaling false r277_004_DWI_3shell_E4.mih dwi.mif 
```
:warning: Revisa los bvalues resultantes en `dwi.mif`, pues mrtrix puede escalarlos. El `-bvalue_scaling false` esta ahí para evitar el escalamiento, pero a veces esto puede ser algo confuso. Lee más al respecto en la [documentación de mrtrix](https://mrtrix.readthedocs.io/en/latest/concepts/dw_scheme.html). Para revisar, usa `mrinfo dwi.mif -shell_bvalues`.



## Revisando los datos crudos
:thumbsup: Independientemente de la vía de conversión que elegimos, estamos listos para preprocesar `dwi.mif`

Primero que nada, tenemos que ver las imágenes antes de preprocesar, si no cómo vamos a saber que sí las mejoramos al final.

```bash=
mrview dwi.mif
```

![](https://github.com/c13inb/c13inb.github.io/blob/master/images/raw_50.gif)

(si no se ve un gif animado con las imágenes, da clic [aquí](https://i.imgur.com/EbYzumN.gif).

Se ven primero las imágenes DWI, seguidas por cada dirección de gradiente de difusión con tres distintos valores b, cada una. Por eso la imagen se hace obscura periódicamente. Todas las imágenes son algo ruidosas, pero mientras más valor b, menos SNR; el denoising nos ayudará con ésto. Se aprecia cómo a lo largo de la adquisición la imagen se desplaza hacia abajo (ventralmente). En algunas imágenes se ve un fenómeno de enrollamiento en la parte ventral, donde aparece como fantasma el cerebro, debido a un artefacto común en EPI ([N/2 ghosting](http://mriquestions.com/nyquist-n2-ghosts.html)). 

![](https://i.imgur.com/HM0TKpi.png)
Esta vista triplanar muestra un volumen DWI con al menos dos rebanadas con _signal dropout_. En la vista coronal se nota claramente que la imagen está totalmente desplazada hacia abajo. Esta rebanada es un outlier, y deberá ser detectada por `eddy` como tal.

## Denoising


**Este debe ser siempre el primer paso del preprocesamiento**, para que la estructura del ruido esté intacta.

Usaremos `dwidenoise`, de mrtrix, usando todos sus defaults, lo que incluye que el estimador de ruido está basado en Cordero-Grande 2019. 
:information_source: El algoritmo de Cordero-Grande está disponible en mrtrix  versión 3.0.0 y superiores. Revisa la documentación de `dwidenoise` para asegurarte que lo tengas incluido. 
```bash=
dwidenoise -info -noise noiseestimation.mif dwi.mif dwi_d.mif
```
Este paso tarda unos 10 minutos. Al terminar, podemos ver los archivos `dwi.mif` (original), `dwi_d.mif` (denoised) y `noiseestimation.mif`:

![](https://i.imgur.com/LTLTqaQ.png)


:point_right: Una bonita alternativa para el denoising es el algoritmo de [LPCA de José Manjón](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0073021), encapsulado en el script `inb_dwidenoise_LPCA_manjon.sh`. Suele quitar aún más ruido que `dwidenoise` (a veces demasiado, pero pruébalo!).

## Unringing
Este proceso trata de minimizar los [anillos de Gibbs](http://mriquestions.com/gibbs-artifact.html) que pueden verse alrededor de bordes anatómicos muy prominentes. Para que sea eficiente, las imágenes deben adquirirse con llenado total del espacio k (es decir, sin Partial Fourier). Si se hizo denoising, este paso debe seguir inmediatamente, y por ningún motivo se debe hacer después de Eddy. 

*Las imágenes de este ejercicio tienen Partial Fourier, por lo que no deberíamos hacer unringing y brincarnos a Eddy*. Se incluye aquí para fines didácticos únicamente. Si se hiciera el unringing, el resto del preprocesamiento debe hacerse con el archivo `dwi_du.mif` en lugar de `dwi_d.mif`.

```bash=
mrdegibbs dwi_d.mif dwi_du.mif
```


## Eddy
Este paso corrige inhomogeneidades geométricas inducidas por los gradientes de difusión. Además elimina rebanadas con adquisiciones comprometidas (outlilers), en las que la señal es demasiado baja en comparación a lo esperado. Esto último es común en adquisiciones 2D-EPI, y se debe a que los gradientes de plano no aguantaron el ritmo solicitado para llenar el espacio k tan rápido. 

:point_right: Es de esperar un 10% de rebanadas outliers en toda la adquisición (algo común es una o dos rebanadas outliers por cada volumen, y la posición espacial de las rebanadas outliers deben ser aleatorias entre volúmenes).

`eddy` es un programa que forma parte de la suite fsl. Es notoriamente lento en CPU (varias horas!), pero en GPU corre muy, muy bien y en unos 10-15 min termina. Por lo tanto, no recomiendo usar `eddy` en una computadora que no tenga tarjeta de video Nvidia con los drivers CUDA instalados. 

:information_source: Si vas a instalar CUDA en tu laptop, encuentra las instrucciones por [acá](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html). 

En don clusterio, debemos preparar el ambiente para usar CUDA. Usa el siguiente comando:

```bash=
source /home/inb/lconcha/fmrilab_software/tools/inb_config_cuda9.sh
```
Revisa más información sobre CUDA en Don Clusterio en [este link](https://github.com/c13inb/c13inb.github.io/wiki/CUDA).

:information_source: El comando `nvidia-smi` te debe desplegar información acerca de la tarjeta de video y los procesos que están corriendo en el GPU (de hecho lo puedes usar como una alternativa a `top` para GPU).

:information_source: En una instalación en una computadora personal, lo ideal es hacer un soft link llamado `eddy` que apunte a `eddy_cuda9.1`, ambos dentro de la carpeta `$FSLDIR/bin/`. Así, si mandamos llamar a `eddy`, automáticamente se ejecutará la versión cuda.

La siguiente consideración es la versión de fsl. Para este ejercicio estaremos usando FSL 6.0.2. Asegúrate qué versión de fsl estás usando `cat $FSLDIR/etc/fslversion`

:information_desk_person: En don clusterio es fácil preparar tu ambiente para FSL 6.0.2 usando el alias `fsl602`.



Primero, convertimos nuevamente a nifti, porque fsl no sabe leer archivos `mif`.
```bash=
mrconvert dwi_d.mif dwi_d.nii \
  -export_grad_fsl bvecs bvals
```
Y preparamos algunas variables para hacer más fáciles de leer los comandotes que siguen.

```bash=
dwi=dwi_d.nii
bvec=bvecs
bval=bvals
```

Creamos una máscara. Hay muchas maneras de hacerlo, se puede hacer con [bet](https://github.com/c13inb/c13inb.github.io/wiki/FSL:-Brain-extraction-tool-BET) o similares, o hasta manualmente. En este ejercicio lo haré con `dwi2mask` de mrtrix. Independientemente de la herramienta usada, muy probablemente habría que editar manualmente su resultado para tener una buena máscara de cerebro. Por ahora no lo haré, pero si fuera a hacer un análisis formal, claro que lo haría.

```bash=
mask=${dwi%.nii}_mask.nii.gz
dwi2mask -fslgrad $bvec $bval $dwi $mask
```

Ahora preparamos los archivos que va a requerir `eddy`, que le dicen cómo fueron adquiridas las imágenes. Estos archivos son particularmente importantes cuando uno tiene adquisiciones con inversión de la polaridad del gradiente de fase, pero en nuestro caso no hay tal cosa, así que los podemos generar fácilmente con estos comandos que siguen. Para adquisiciones con inversión de polaridad de fase, consulta la documentación en la página de [topup](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/topup/TopupUsersGuide), donde se describe cómo generar un B0map a partir de pares de adquisiciones con fases invertidas, que después se alimentan a `eddy`. Yo (lconcha, abril-julio 2021) hice varias pruebas con adquisiciones 2DEPI en el Bruker y no encontré mucha ventaja a usar adquisiciones con pares de dirección de fase y el uso de `topup`, por lo que en este ejercicio no se utiliza.

```bash=
acqp=${dwi%.nii}_acqp.txt
index=${dwi%.nii}_index.txt
c4topup=0.0438;# this is just a guess
nvols=`fslnvols $dwi`
echo 0 -1 0 $c4topup > $acqp
indx=""
for ((i=1; i<=$nvols; i+=1)); do indx="$indx 1"; done
echo $indx > $index
```

Si vemos el contenido de los nuevos archivos, veremos que `$acqp` tiene un solo renglón, que dice que la segunda dimensión está codificada mediante fase (negativa). El número 0.0438 por ahora no se va a usar, pero en el caso de `topup` se usa para que el fieldmap quede con unidades correctas. El archivo `$index` es una lista de puros números uno, tan larga como el número de volúmenes. Si hubiéramos tenido diferentes adquisiciones mediante fase, habría más renglones en `$acq` y en `$index` nos diría a qué renglón (tipo de adquisición) corresponde cada volumen. Por ahora no se usa, así que es un solo renglón, y puros unos. Facilito.

Ahora sí, a correr `eddy`:

```bash=
outbase=${dwi%.nii}eddycorr
time eddy_cuda9.1 --verbose \
  --imain=$dwi \
  --mask=$mask \
  --acqp=$acqp \
  --index=$index \
  --bvecs=$bvec \
  --bvals=$bval \
  --residuals=true \
  --repol=true \
  --out=$outbase
```

En `mansfield`, con una pobretona tarjeta Nvidia GeForce GTX 650 Ti con 1 GB de memoria, esto terminó en 15 minutitos. Me hizo varios outputs, señalaré solo los más relevantes (el resto descritos [acá](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/eddy/UsersGuide#Understanding_eddy_output)):

+ `${outbase}.nii.gz`. Nuestro output principal. Incluye las imágenes ya corregidas, a las que se les minimizaró el movimiento entre volúmenes, así como las inhomogeneidades geométricas inducidas por corrientes eddy. Además, las rebanadas outliers fueron remplazadas por datos factibles dado un modelo simple. Estas son las imágenes que se usarán después para cualquier modelo de DWI.
+ `${outbase}.eddy_rotated_bvecs`. Los vectores de los gradientes de difusión, una vez que fueron corregidos de acuerdo a las transformaciones geométricas que se le hicieron a cada volumen correspondiente. Por ejemplo, si un volumen se rotó 10 grados, el gradiente se rota también. En conjunto con `$bval` podremos usar cualquier modelo de difusión. 

:warning: Los volúmenes considerados como b=0 no tienen vector asociado. Estúpidamente, en este archivo aparecen sus componentes x,y,z como `nan`. Esto va a hacernos la vida difícil para los siguientes pasos. Es fácil remplazar todas las ocurrencias de `nan` por un cero usando el fabuloso [`sed`](https://www.grymoire.com/Unix/Sed.html#uh-1):
```bash=
sed -i 's/nan/0/g' ${outbase}.eddy_rotated_bvecs
```
:warning: De forma similar, el archivo `$bval` no tiene entradas con b=0 s/mm². El resonador calcula la contribución de los gradientes de codificación espacial al valor b, y habitualmente resulta en b=15 a 30 s/mm². Cambiar estas entradas a cero hará cambios realmente despreciables en toda estimación de parámetros de difusión, así que lo vamos a hacer ahora. (de hecho, si se quiere se puede hacer desde el principio de todo el preprocesamiento, es solo que hasta aquí se nota el efecto de la ausencia de valores b=0 en el archivo `$bval`). 

Solo debemos saber qué valor tenemos que cambiar, y suele ser el shell más bajo. Una manera simple es abrir el archivo `$bval` y revisar el número a cambiar, habitualmente en la primera entrada. Si la adquisición no inició con imágenes no pesadas a difusión, entonces usemos un método más robusto para encontrar el valor del shell con valor despreciable.
```bash=
mrinfo -fslgrad $bvec $bval $dwi -shell_bvalues
```
(pero cuidado porque redondea a 4 números decimales).

Vamos a quitarnos de problemas y abrir el archivo `$bval` en `gedit` o el editor de texto de nuestra preferencia, y sustituir todas las ocurrencias del valor b más bajo (en este caso 21.010828) por 0. Escribimos un nuevo archivo `bval_zeros`. Esto también lo podemos hacer en la terminal con el fabuloso `sed`: 

```bash=
sed 's/21.010828/0/g' $bval > bval_zeros
```

+ `${outbase}.eddy_outlier_report`.  Un archivo de texto que nos dice qué rebanadas en cada volumen resultaron ser outliers.
`${outbase}.eddy_outlier_map`.  Un archivo de texto con una simple visualización como tabla que nos dice por cada rebanada (columnas) en cada volumen (renglones), si es un outlier.

### Consideraciones sobre `eddy`
+ La mera verdad no logra registrar bien los volúmenes con SNR muy bajo, lo que suele suceder con alta resolución y bvalues altos (por ejemplo b=3000 s/mm²). Para el modelo del tensor no son útiles los bvalues altos, por lo que se sugiere no llegar más allá de 1200. Sin embargo, la mayoría de los solvers modernos para ajustar el tensor le dan un peso mayor o menor a cada dato dependiendo de su potencial de ser outlier. Por lo tanto, incluso dejando los volúmenes de bvals altos, los mapas resultantes son harto bonitos.

![](https://i.imgur.com/nsElYei.gif)
En esta animación se aprecia que la posición espacial no es homogénea entre volúmenes. Los volúmenes con bvalue más alto están mal registrados con respecto a los otros shells.

## Corrección de inhomogeneidad de intensidades (biasfield correction)
Este paso es también innecesario en caso de que se vaya a usar cualquier modelo que involucre dividir las DWI entre las b=0, como el modelo del tensor. De hecho, la enorme mayoría de los modelos hacen tal división en algún momento, pues lo que les interesa es la atenuación de la señal. 

La notable excepción es deconvolución esférica (CSD), que estima la distribución de la probabilidad de orientaciones de fibras directamente de la señal DWI (no de la atenuación), a partir de la deconvolución de una función de respuesta que actúa como un prototipo de cómo se porta la señal DWI en el caso de una sola población de fibras. Como se estima una sola función de respuesta por set de datos, es crucial que la señal DWI tenga intensidades homogéneas en toda la extensión de la sustancia blanca. Esta última suposición se rompe fácilmente, sobre todo si adquirimos nuestras imágenes con una antena de superficie (como la 2x2 o la cryoprobe). 

Usaremos `dwibiascorrect` de mrtrix, que en realidad es una envoltura para `N4BiasFieldCorrection` de [ANTS](http://picsl.upenn.edu/software/ants/). Por lo tanto, debes tener ANTS instalado. Los defaults de ambos comandos están diseñados para datos de humanos, así que es posible que se requiera un poco de ensayo y error hasta encontrar los adecuados. El comando en sí es muy fácil, mandando las opciones para ANTS a través de switches en `dwibiascorrect`. A continuación un ejemplo con opciones pasadas a ANTS que resultan en una buena corrección:

```bash=
dwibiascorrect ants \
  -fslgrad ${outbase}.eddy_rotated_bvecs bval_zeros \
  -mask $mask \
  -ants.s 2 \
  -ants.b [10,3] \
  $outbase.nii.gz \
  ${outbase%.nii*}_biascorr.nii.gz 
```
![](https://i.imgur.com/yVnbtRp.png)


## Viendo el resultado
Para terminar, veamos la diferencia entre un ajuste del modelo del tensor a los datos originales, y a los datos preprocesados. Usaremos mrtrix para hacer esta estimación, y truquitos para hacer todo en un jalón. Aprende a usar los pipes de mrtrix por [acá](https://mrtrix.readthedocs.io/en/latest/getting_started/command_line.html#unix-pipelines). Haremos mapas RGB del vector principal de difusión, a los que llamaremos `*_v1.mif`.

Primero, a partir de los datos originales:
```bash=
dwi2tensor -mask $mask \
  dwi.mif - | tensor2metric -vector orig_v1.mif - 
```

Ahora, a partir de los datos con denoise y eddy (no requerimos corrección de intensidad para el modelo del tensor, y no podemos hacer unring porque los datos tienen partial fourier):

```bash=
dwi2tensor \
  -fslgrad ${outbase}.eddy_rotated_bvecs $bval \
  -mask $mask \
  ${outbase}.nii.gz - | tensor2metric \
  -vector preprocessed_v1.mif -
```

Y los vemos con `mrview`:
![](https://i.imgur.com/VyYH2of.png)

Los mapas RGB son notablemente más claros cuando son derivados de imágenes preprocesadas. Hay mucho menos verde, que era causado por el drift de las imágenes a lo largo de la adquisición en dirección dorso-ventral, cosa que fue minimizada con el registro logrado con `eddy`. Aún quedan detalles, pero ciertamente estas imágenes ya están trabajables, sobre todo en s. blanca.
