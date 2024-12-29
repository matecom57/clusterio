DWMRI:designer
==============

Luis Concha edited this page 3 weeks ago · 6 revisions

Preprocesamiento de datos con DESIGNER2
---------------------------------------

`Designer <https://nyu-diffusionmri.github.io/DESIGNER-v2/>`_ es un pipeline muy completo y 
fácil de usar para preprocesamiento de DWIs. Igual que `dwifslpreproc <https://mrtrix.readthedocs.io/en/dev/reference/commands/dwifslpreproc.html>`_ , encapsula muchas herramientas disponibles en fsl y mrtrix, como topup, eddy, y mrdegibbs. Pero quizás su herramienta más poderosa sea su denoiser.

La manera más fácil de usarlo es con Singularity (Apptainer).

module load singularity

designer_container=/home/inb/soporte/lanirem_software/containers/designer2.sif

singularity run --nv $designer_container \
  designer \
  -eddy \
  -mask \
  -denoise \
  -rpe_pair bids/sub-26651/fmap/sub-26651_acq-hb_epi.nii.gz \
  -pe_dir AP \
  bids/sub-26651/dwi/sub-26651_acq-hb_dwi.nii.gz \
  outputdesigner.nii
El switch --nv permite a singularity utilizar CUDA. No es necesario usarlo si la máquina no tiene tarjeta NVIDIA (podemos revisar eso con lspci | grep VGA).

alt text

La mejoría de Designer2 con respecto a dwifslpreproc es notoria. alt text

ℹ️ Revisa esta tabla comparativa de denoisers.

