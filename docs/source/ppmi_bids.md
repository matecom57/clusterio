# PPMI, BIDS
Para bajar datos de PPMI y convertirlos a [BIDS](./BIDS).

:information_source: Requiere [docker](https://www.docker.com/) y python 3.x, así como una cuenta en PPMI.

:star: Basado en [PyPMI](https://pypi.org/project/pypmi/).

## Bajar datos
1.Ir a [PPMI](https://ida.loni.usc.edu/pages/access/search.jsp?tab=collection&loginKey=1607884889662832790&userEmail=lconcha%40unam.mx&project=PPMI&page=DOWNLOADS&subPage=IMAGE_COLLECTIONS).
2. Ir a `Advanced Search` y buscar lo que queremos usando los criterios de inclusión/exclusión. Una vez encontrados, seleccionar los que queremos (o todos) y dar clic en `add to collection`. Generar una nueva colección, o usar una previa.
3. Ir a la pestaña `Data Collections`, buscar nuestra colección, y seleccionar los que queremos bajar ( o todos ). Usar `Advanced Download` para facilitar el que bajen todos en un único zip. 
![](https://i.imgur.com/vuKNzIb.png)
4. Bajar el archivo `.zip`. Copiarlo a una carpeta, y descomprimirlo (podemos usar `unzip` en la terminal)
5. El zip explotará en una carpeta llamda `PPMI`, que tiene una organización NO-BIDS (ver [aquí](https://github.com/rmarkello/pypmi/blob/master/pypmi/bids.py))
```
   └── PPMI/
        ├── SUB-1/
        |   ├── SCAN-TYPE-1/                      (e.g., MPRAGE_GRAPPA)
        |   |   ├── SCAN-DATETIME-1/
        |   |   |   └── SCAN-SERIES-1/
        |   |   |       └── *dcm
        |   |   └── SCAN-DATETIME-2/
        |   ├── SCAN-TYPE-2/                      (e.g., AX_FLAIR)
        |   |   ├── SCAN-DATETIME-1/
        |   |   |   └── SCAN-SERIES-2/
        |   |   |       └── *dcm
        |   |   └── SCAN-DATETIME-2/
        |   ├── .../
        |   └── SCAN-TYPE-N/
        ├── SUB-2/
        ├── .../
        └── SUB-N/
```
Queremos convertir esta jerarquía en BIDS. Usaremos las herramientas de `pypmi`.

## Convertir a BIDS
Para fines de este documento, la carpeta PPMI quedó en `/mnt/newssd/rene/PPMI`, y la carpeta BIDS quedará en `/mnt/newssd/rene/bids`
1. Asegurarnos que tenemos python. Yo estoy probando con Anaconda con python versión 3.8.3.
2. Instalamos las dependencias
```bash=
pip install pypmi pydicom nibabel docker
```
3. Abrimos `ipython` para trabajar.
```bash=
ipython
```
4. Dentro de ipython:
```python
from pypmi import bids
bids.convert_ppmi('/mnt/newssd/rene/PPMI','/mnt/newssd/rene/bids') 
```
La primera vez que lo corremos se tarda un poco, pues tiene que bajar un docker container de [heudiconv](https://github.com/nipy/heudiconv), y no hay mucha información en la terminal (me dí cuenta porque ví que estaba bajando muchos MB/s).
Al terminar, tendremos nuestra carpeta bids
```bash
(base) lconcha@syphon:/mnt/newssd/rene$ tree bids/
bids/
├── CHANGES
├── dataset_description.json
├── participants.tsv
├── README
├── sub-3108
│   ├── ses-1
│   │   ├── anat
│   │   │   ├── sub-3108_ses-1_run-01_T1w.json
│   │   │   └── sub-3108_ses-1_run-01_T1w.nii.gz
│   │   ├── dwi
│   │   │   ├── sub-3108_ses-1_run-01_dwi.bval
│   │   │   ├── sub-3108_ses-1_run-01_dwi.bvec
│   │   │   ├── sub-3108_ses-1_run-01_dwi.json
│   │   │   ├── sub-3108_ses-1_run-01_dwi.nii.gz
│   │   │   ├── sub-3108_ses-1_run-02_dwi.bval
│   │   │   ├── sub-3108_ses-1_run-02_dwi.bvec
│   │   │   ├── sub-3108_ses-1_run-02_dwi.json
│   │   │   └── sub-3108_ses-1_run-02_dwi.nii.gz
│   │   └── sub-3108_ses-1_scans.tsv
│   └── ses-2
│       ├── anat
│       │   ├── sub-3108_ses-2_run-01_T1w.json
│       │   └── sub-3108_ses-2_run-01_T1w.nii.gz
│       ├── dwi
│       │   ├── sub-3108_ses-2_run-01_dwi.bval
│       │   ├── sub-3108_ses-2_run-01_dwi.bvec
│       │   ├── sub-3108_ses-2_run-01_dwi.json
│       │   ├── sub-3108_ses-2_run-01_dwi.nii.gz
│       │   ├── sub-3108_ses-2_run-02_dwi.bval
│       │   ├── sub-3108_ses-2_run-02_dwi.bvec
│       │   ├── sub-3108_ses-2_run-02_dwi.json
│       │   └── sub-3108_ses-2_run-02_dwi.nii.gz
│       └── sub-3108_ses-2_scans.tsv
├── sub-3352
│   └── ses-1
│       ├── anat
│       │   ├── sub-3352_ses-1_run-01_T1w.json
│       │   └── sub-3352_ses-1_run-01_T1w.nii.gz
│       └── sub-3352_ses-1_scans.tsv

```