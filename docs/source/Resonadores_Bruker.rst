Bruker Biospec 70/16 -0
====================


Para usar el resonador Bruker es necesario acreditar un proceso de certificación. Para ello es necesario contactar al Dr. Juan Ortiz.


Algunos datos sobre el resonador:

* Bruker Biospec 70/16: 70 porque es un 7 Tesla, y 16 porque su túnel tiene 16 cm de diámetro.

* El resonador tiene un magneto  `Pharmascan <https://www.bruker.com/products/mr/preclinical-mri/pharmascan/overview.html?gclid=EAIaIQobChMIo-bPoJCW4QIVx7jACh3UYAvBEAAYASAAEgIKrfD_BwE>`_, sin embargo toda la electrónica y los gradientes son de un [Biospec](https://www.bruker.com/products/mr/preclinical-mri/biospec/overview.html?gclid=EAIaIQobChMIrY6ZtpCW4QIVhIbACh3L_wZLEAAYASAAEgJdofD_BwE). Por lo tanto, el resonador es _de facto_ un Biospec.


La transferencia de los datos se puede realizar en varios formatos:


* Formato NIFTI: Obten primero tus datos en DICOM  y posteriormente conviértelos en tu máquina usando `mrconvert <https://mrtrix.readthedocs.io/en/latest/reference/commands/mrconvert.html>`_ de Mrtrix3, o [dcm2niix](https://github.com/rordenlab/dcm2niix).


***

 Como exportar mis datos desde el Bruker
--------------------




cd /misc/bruker7/data02/user/mi_usuario


ls *irm150d_rata64A*

Al hacer este filtro, yo estoy buscando especificamente por la rata 64A y el archivo que me encontro es el siguiente: 



ls 20220104_085643_INB_C13_hluna_irm150d_rata64A_INB_C13_hluna_1_1/

1  2  3  4  5  6  7  8  AdjResult  AdjStatePerStudy  Mapshim  ResultState  ScanProgram.scanProgram  subject

Bien, hasta aqui ya sabemos como acceder a tus imágenes del Bruker, siguiente paso es exportarlas en formato Nifti.

Paso numero uno es cargar el modulo de Bruker (gracias a Ricardo Rios que nos hizo la vida mas facil al crear los modulos, si aun no te familiarizas con ellos, da click `aquí <https://github.com/c13inb/c13inb.github.io/wiki/Modules>`_ y aprende mas a como usarlos.


module load brkraw/0.3.11


brkraw info 20220104_085643_INB_C13_hluna_irm150d_rata64A_INB_C13_hluna_1_1/

Paravision 7.0.0
----------------
UserAccount:    conchalab 
Date:           2022-01-04
Researcher:     rata64A
Subject ID:     INB_C13_hluna_irm150d_rata64A
Session ID:     INB_C13_hluna_irm150d_rata64A
Study ID:       1
Date of Birth:  07 Aug 2021
Sex:            male
Weight:         0.433 kg
Subject Type:   Quadruped
Position:       Prone           Entry:  HeadFirst

[ScanID]        Sequence::Protocol::[Parameters]
[001]   Bruker:FLASH::1_Localizer::1_Localizer (E1)
        [ TR: 100 ms, TE: 2.50 ms, pixelBW: 159.22 Hz, FlipAngle: 30 degree]
    [01] dim: 2D, matrix_size: 256 x 256 x 3, fov_size: 50 x 50 (unit:mm)
         spatial_resol: 0.195 x 0.195 x 2.000 (unit:mm), temporal_resol: 12800.000 (unit:msec)
[002]   Bruker:FLASH::1_Localizer::1_Localizer (E2)
        [ TR: 100 ms, TE: 2.50 ms, pixelBW: 159.22 Hz, FlipAngle: 30 degree]
    [01] dim: 2D, matrix_size: 256 x 256 x 3, fov_size: 50 x 50 (unit:mm)
         spatial_resol: 0.195 x 0.195 x 2.000 (unit:mm), temporal_resol: 12800.000 (unit:msec)
[003]   Bruker:FLASH::1_Localizer::1_Localizer (E3)
        [ TR: 100 ms, TE: 2.50 ms, pixelBW: 159.22 Hz, FlipAngle: 30 degree]
    [01] dim: 2D, matrix_size: 256 x 256 x 3, fov_size: 50 x 50 (unit:mm)
         spatial_resol: 0.195 x 0.195 x 2.000 (unit:mm), temporal_resol: 12800.000 (unit:msec)
[004]   Bruker:FLASH::T1_FLASH::T1_FLASH (E4)
        [ TR: 201.57 ms, TE: 3.50 ms, pixelBW: 98.64 Hz, FlipAngle: 30 degree]
    [01] dim: 2D, matrix_size: 384 x 384 x 13, fov_size: 25.6 x 25.6 (unit:mm)
         spatial_resol: 0.067 x 0.067 x 1.100 (unit:mm), temporal_resol: 309614.466 (unit:msec)
[005]   Bruker:FieldMap::B0Map-ADJ_B0MAP::T1_FLASH
        [ TR: 20 ms, TE: 0 ms, pixelBW: 1860.12 Hz, FlipAngle: 30 degree]
    [01] dim: 3D, matrix_size: 64 x 64 x 64, fov_size: 45 x 45 x 45 (unit:mm)
         spatial_resol: 0.703 x 0.703 x 0.703 (unit:mm), temporal_resol: 81920.000 (unit:msec)
[006]   Bruker:DtiEpi::DTI_EPI_30dir::DWIzoom (E6)
        [ TR: 2000 ms, TE: 22.86 ms, pixelBW: 2289.38 Hz, FlipAngle: 90 degree]
    [01] dim: 2D, matrix_size: 126 x 86 x 25 x 285, fov_size: 22 x 15 (unit:mm)
         spatial_resol: 0.175 x 0.174 x 1.250 (unit:mm), temporal_resol: 4000.000 (unit:msec)
    [02] dim: 2D, matrix_size: 126 x 86 x 22 x 25, fov_size: 22 x 15 (unit:mm)
         spatial_resol: 0.175 x 0.174 x 0.006 (unit:mm), temporal_resol: 0.000 (unit:msec)
[007]   Bruker:DtiEpi::DTI_EPI_30dir::DWI-IVIM-zoom(E11) (E7)
        [ TR: 2000 ms, TE: 22.86 ms, pixelBW: 2289.38 Hz, FlipAngle: 90 degree]
    [01] dim: 2D, matrix_size: 126 x 86 x 25 x 63, fov_size: 22 x 15 (unit:mm)
         spatial_resol: 0.175 x 0.174 x 1.250 (unit:mm), temporal_resol: 4000.000 (unit:msec)
    [02] dim: 2D, matrix_size: 126 x 86 x 22 x 25, fov_size: 22 x 15 (unit:mm)
         spatial_resol: 0.175 x 0.174 x 0.006 (unit:mm), temporal_resol: 0.000 (unit:msec)
[008]   Bruker:RARE::T2_TurboRARE::T2_TurboRARE (E8)
        [ TR: 4212.78 ms, TE: 33 ms, pixelBW: 140.85 Hz, FlipAngle: 141.72 degree]
    [01] dim: 2D, matrix_size: 256 x 256 x 26, fov_size: 30 x 30 (unit:mm)
         spatial_resol: 0.117 x 0.117 x 1.200 (unit:mm), temporal_resol: 269617.981 (unit:msec)



brkraw tonii 20220104_085643_INB_C13_hluna_irm150d_rata64A_INB_C13_hluna_1_1/ -o /path/64A_dwi -r 1 -s 8
En otras palabras:







mrview 64A_T2.nii.gz

Y el resultado es esto:

 `image <https://github.com/c13inb/c13inb.github.io/assets/129544525/fe8d393b-9b6f-4df3-9af3-02aadabf23f1>`_

Una vez que conviertes tus imágenes, estas listo para el siguiente paso que es procesarlas de acuerdo al tipo de estudio. Aprende más acerca de como procesar tus imágenes en esta `entrada <https://github.com/c13inb/c13inb.github.io/wiki/Procesamiento-Imagen>`_. 


***

Tutoriales para el uso del resonador
--------------------


Las siguientes páginas de la wiki incluyen algunos tutoriales para el uso básico del resonador.

* :doc:`Resonadores-Bruker-Conexión-Cryo`


* :doc:`Resonadores-Bruker-Paravision-EXvivo`


* :doc:`Resonadores-Bruker-Wobble-Superficie`


Checklists para uso del resonador
--------------------


Las siguientes ligas contienen algunos google docs con checklist útiles para el cambio de antenas y uso del resonador.

* `Preparación antena Cryo <https://docs.google.com/document/d/1S850dGVnyL1k5UMD0Cf-ebfKXblKklNMRuPto7Vl66M/edit?usp=sharing>`_

* `Preparación antena de volumen <https://docs.google.com/document/d/1pCrKejx-Q31kqw07g8t0ZBscDQr9n007i6fegMNHtMA/edit?usp=sharing>`_

* `Checklist inicio Paravision <https://docs.google.com/document/d/1hwDM7ySkY2xqzBnHkGzsFiiu1vH7U6Af9pxxcvGMHR4/edit?usp=sharing>`_
