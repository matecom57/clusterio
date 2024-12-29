# deepprep
13 de marzo de 2024

Cómo correrlo.

Debemos tener todo en bids.

```bash!
cd /misc/mansfield/lconcha/exp/glaucoma

ml singularity

lic=/home/inb/soporte/lanirem_software/freesurfer_7.4.1/license.txt 
deepprep=/misc/lauterbur/lconcha/nobackup/containers/deepprep.sif
bids_dir=/misc/mansfield/lconcha/exp/glaucoma/bids
out_dir=/misc/mansfield/lconcha/exp/glaucoma/tmp/out

singularity run \
  --nv \
  -B /home/inb/soporte \
  -B /misc/mansfield/lconcha/exp/glaucoma \
  $deepprep \
  $bids_dir \
  $out_dir \
  participant  \
  --fs_license_file $lic  \
  --anat_only \
  --skip_bids_validation \
  --device 0 \
  --cpus 8 \
  --participant-label sub-74805
```

A pesar de que especifiqué que solo corriera al sujeto `sub-74805`, hizo todas las superficies de freesurfer para >20 sujetos en menos de 3 horas. Sorprendente. Esto fue en `lauterbur`, usando la GPU.