
# Pandoc
- Es posible generar presentaciones con markdown usando [pandoc](https://pandoc.org/).
- Se convierte el archivo `.md` a una presentación html.
- Soporta `s5`, `slidy`, `slideous`, `dzslides` y el sexy `revealjs`.
- También soporta `pdf` mediante `beamer`!.
![pandoc](https://i.loli.net/2018/02/21/5a8d775f73d87.png)


# Reglas del `.md`
- Básicamente, seguir las reglas de markdown, usando bullet points.
- Los bullet points se indican con `-`
- Los niveles `#` indican nueva diapositiva.
- También se puede indicar nueva diapositiva con `---------`
- Instrucciones completas [aquí](https://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc).

# Ejemplo
```
---
title: Presentaciones geek
author: Luis Concha
---

# Pandoc
- Es posible generar presentaciones con markdown usando [pandoc](https://pandoc.org/).
- Se convierte el archivo `.md` a una presentación html.
- Soporta `s5`, `slidy`, `slideous`, `dzslides` y el sexy `revealjs`.
- También soporta `pdf` mediante `beamer`!.
![pandoc](https://i.loli.net/2018/02/21/5a8d775f73d87.png)

# Reglas del `.md`
- Básicamente, seguir las reglas de markdown, usando bullet points.
- Los bullet points se indican con `-`
- Los niveles `#` indican nueva diapositiva.
- También se puede indicar nueva diapositiva con `---------`
- Instrucciones completas [aquí](https://pandoc.org/MANUAL.html#producing-slide-shows-with-pandoc).
```

# Conversión de `.md` a `html`
```
pandoc -t FORMAT -s miarchivo.md -o mipresentacion.html
```

- Donde `FORMAT` debe ser uno de `s5`, `slidy`, `slideous`, `dzslides` o `revealjs`.

-------
Quieres ver un resultado?
Por [aquí!.](https://github.com/c13inb/c13inb.github.io/blob/master/presentaciones_geek.html)

-------

- `FORMAT` también puede ser `beamer`, pero en ese caso el output debe tener la extensión `pdf`
- Se puede indicar un _theme_ de `beamer`:
```
pandoc -t beamer -s miarchivo.md -V theme=Madrid mipresentacion.pdf
```
- [Aquí](https://hartwork.org/beamer-theme-matrix/) hay una galería de temas para beamer.


# Conversión a `.pptx`
- Se puede convertir a power point!
```
pandoc miarchivo.md -o mipresentacion.pptx
```


# Cosas que aún no comprendo
- Controlar el tamaño de las imágenes.
- Los diferentes formatos de salida html tienen opciones distintas y manejan el encabezado (título, autor) de manera diferente.
- Cómo hacer que un bullet-point largo quepa en una sola diapo.

# Opinión personal:
- Útil para presentaciones que contienen código y **tutoriales**.
- Difícil hacer que se vea _exactamente como quiero_ .
- Menos utilidad para presentaciones científicas (no geek).
