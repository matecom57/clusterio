Descarga los cambios realizados en el repositorio remoto:
```bash
git  fetch
```

Impacta en la rama en la que te encuentras parado, los cambios realizados en la rama “nombre_rama”:
``` bash
git merge '<nombre_rama>'
```
Unifica los comandos ''fetch'' y ''merge'' en un único comando:
 ```bash
git pull
```

Confirma los cambios realizados: El “mensaje” generalmente se usa para asociar al ''commit'' una breve descripción de los cambios realizados:
 ``` bash
git commit -am "<mensaje>"
```

Sube la rama “nombre_rama” al servidor remoto:
 ```bash
git push origin ''<nombre_rama>''
```

Muestra el estado actual de la rama, como los cambios que hay sin commitear:
 ```bash
git status
```

Comienza a trackear el archivo “nombre_archivo”:
 ```bash
git add ''<nombre_archivo>''
```

Crea una rama a partir de la que te encuentres parado con el nombre “nombre_rama_nueva”, y luego salta sobre la rama nueva, por lo que quedas parado en ésta última:
 ``` bash
git checkout -b ''<nombre_rama_nueva>''
```

Si existe una rama remota de nombre “nombre_rama”, al ejecutar este comando se crea una rama local con el nombre “nombre_rama” para hacer un seguimiento de la rama remota con el mismo nombre:
 ```bash
git checkout -t origin/''<nombre_rama>''
```

Lista todas las ramas locales:
```bash
git Branch
```

Lista todas las ramas locales y remotas:
```bash
git branch -a
```

Elimina la rama local con el nombre “nombre_rama”:
 ``` bash
git branch -d ''<nombre_rama>''
```

Elimina la rama remote con el nombre “nombre_rama”:
 ```bash 
git push origin ''<nombre_rama>''
```

Actualiza tu repositorio remoto en caso que algún otro desarrollador haya eliminado alguna rama remota:
```bash git remote prune origin
```

Elimina los cambios realizados que aún no se hayan hecho ''commit'':
 ``` bash 
git reset --hard HEAD
```

Revierte el ''commit'' realizado, identificado por el “hash_commit”:
```bash
git revert ''<hash_commit>''
```

