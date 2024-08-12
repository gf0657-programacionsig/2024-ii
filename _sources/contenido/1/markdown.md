# Markdown - lenguaje de marcado


## Trabajo previo

### Tutoriales
*Markdown Tutorial*. (s. f.). Recuperado 19 de marzo de 2022, de [https://www.markdowntutorial.com/](https://www.markdowntutorial.com/)

### Otros recursos
*Markdown Guide*. (s. f.). Recuperado 10 de abril de 2022, de [https://www.markdownguide.org/](https://www.markdownguide.org/)


## Resumen
Markdown es un lenguaje de marcado ligero ampliamente utilizado en comunicación científica, documentación de programas e investigación reproducible.


## Descripción general
[Markdown](https://daringfireball.net/projects/markdown/) es un [lenguaje de marcado](https://es.wikipedia.org/wiki/Lenguaje_de_marcado) creado en 2004 por John Gruber. Las "marcas" se utilizan para brindar información acerca de la presentación (ej. negritas, itálicas) o la estructura (ej. títulos, encabezados) de un documento. Se caracteriza por ser más sencillo de leer y de usar que otros lenguajes de marcado (ej. [Lenguaje de marcado de Hipertexto o HTML](https://es.wikipedia.org/wiki/HTML)), por lo que se considera un [lenguaje de marcado ligero](https://es.wikipedia.org/wiki/Lenguaje_de_marcas_ligero). Los documentos escritos en Markdown pueden exportarse a una gran variedad de formatos (ej. HTML, DOC, PDF, LaTex) para ser usados en libros, presentaciones o páginas web, entre otros. Markdown es ampliamente utilizado en comunicación científica, documentación de programas e investigación reproducible.


## Variaciones
Las variaciones de Markdown, también llamadas *flavors*, son extensiones o modificaciones de la especificación original. Entre las más populares están:

- [R Markdown](https://rmarkdown.rstudio.com/): para el lenguaje R.
- [GitHub Flavored Markdown](https://help.github.com/en/github/writing-on-github): para la plataforma GitHub.
- [Python Markdown](https://github.com/Python-Markdown/markdown): para el lenguaje Python.
- [Pandoc's Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown): para el programa [Pandoc](https://pandoc.org/) de conversión entre formatos.
- [Kramdown](https://kramdown.gettalong.org/quickref.html): para el lenguaje Ruby.

Puede verse una lista más extensa en <https://github.com/commonmark/commonmark-spec/wiki/markdown-flavors>.


## Sintaxis
La sintaxis de Markdown permite especificar diferentes componentes de un documento, entre los que están:

-   Encabezados.
-   Estilos (ej. negritas, itálicas).
-   Citas textuales.
-   Enlaces a otros documentos (ej. páginas web).
-   Imágenes.
-   Listas.

### Encabezados
Pueden definirse seis niveles de encabezados, mediante símbolos de numeral (`#`) antes del texto. El primer nivel es el de tamaño de texto más grande y el sexto el más pequeño. En la parte izquierda de la {numref}`fig-md-encabezados` se muestra la sintaxis Markdown de los encabezados y a la derecha la forma en que se despliegan en un documento.

```{figure} img/md-encabezados.png
:name: fig-md-encabezados

Sintaxis de Markdown - encabezados.
```

### Itálicas
Se definen con un asterisco (`*`) antes y después del texto o con un guión bajo (`_`) antes y después del texto.

```{figure} img/md-italica.png
:name: fig-md-italicas

Sintaxis de Markdown - itálicas.
```

### Negritas
Se definen con dos asteriscos (`**`) antes y después del texto o con dos guiones bajos (`__`) antes y después del texto.

```{figure} img/md-negrita.png
:name: fig-md-negritas

Sintaxis de Markdown - negritas.
```

### Citas textuales
Se definen con un símbolo de "mayor que" (`>`) antes de cada línea.

```{figure} img/md-cita.png
:name: fig-md-citas

Sintaxis de Markdown - citas textuales.
```

### Enlaces (hipervínculos)
Se definen con paréntesis cuadrados (`[]`) seguidos de paréntesis redondos (`()`). En los paréntesis cuadrados se coloca (opcionalmente) el texto del enlace y en los redondos la dirección del documento.

```{figure} img/md-enlace.png
:name: fig-md-enlaces

Sintaxis de Markdown - enlaces.
```

### Imágenes
Se definen con un signo de admiración de cierre (`!`), paréntesis cuadrados (`[]`) y paréntesis redondos (`()`). En los paréntesis cuadrados se coloca (opcionalmente) un texto alternativo de la imagen y en los redondos la dirección de la imagen, ya sea local o remota.

```{figure} img/md-imagen.png
:name: fig-md-imagenes

Sintaxis de Markdown - imágenes.
```

### Listas numeradas
Se definen con números (`1. 2. 3. ...`) antes de cada elemento.

```{figure} img/md-lista-numerada.png
:name: fig-md-listas-numeradas

Sintaxis de Markdown - listas numeradas.
```

### Listas no numeradas
Se definen con guiones (`-`) o asteriscos (`*`) antes de cada elemento.

```{figure} img/md-lista-no-numerada.png
:name: fig-md-listas-no-numeradas

Sintaxis de Markdown - listas no numeradas.
```

### Otros elementos de sintaxis
Para conocer otros elementos de la sintaxis de Markdown, se recomienda revisar en detalle la [Guía de referencia de Markdown](https://www.markdownguide.org/).


## Ejercicios
1. Cree un documento Markdown llamado `README.md`, en RStudio, y escriba en este un breve perfil académico (*curriculum* académico).
    - Incluya información como: nombre, fotografía, datos de contacto, áreas de interés, carrera, cursos aprobados, publicaciones, etc.
    - Puede usar información ficticia (**no incluya datos confidenciales o sensibles**).
    - Especifique la fuente de las imágenes (y de cualquier otra información para la que sea necesario) y no utilice imágenes para las que no tiene autorización. Considere utilizar sitios con imágenes con licencias abiertas (ej. [Wikimedia Commons](https://commons.wikimedia.org/), [Unsplash](https://unsplash.com/), [FreeImages](https://www.freeimages.com/)).
    - Asegúrese de utilizar los siguientes elementos de sintaxis Markdown:
        - Varios niveles de encabezados.
        - Negritas e itálicas.
        - Listas.
        - Enlaces a sitios web.
        - Imágenes (al menos una local y una remota).
2. Cree un repositorio en [GitHub](https://github.com/) llamado `perfil-academico` y suba a este el documento que creó en el paso 1.
3. Cree un sitio web en [GitHub Pages](https://pages.github.com/) con el repositorio creado en el paso 2.
