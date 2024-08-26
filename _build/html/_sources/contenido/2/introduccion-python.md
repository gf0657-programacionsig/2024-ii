# Introducción a Python

## Trabajo previo

### Lecturas

Severance, D. C. R. (2016). *Chapter 1: Why should you learn to write programs?* y *Chapter 2: Variables, expressions, and statements* en *Python for Everybody: Exploring Data in Python 3* (S. Blumenberg & E. Hauser, Eds.). CreateSpace Independent Publishing Platform. https://www.py4e.com/html3/

## Introducción

**Python** es un lenguaje de programación de propósito general ampliamente utilizado en áreas como desarrollo web, aprendizaje automático e inteligencia artificial, entre otras. Fue creado por **Guido van Rossum** a finales de la década de 1980.

Python es un lenguaje **interpretado**, **multiplataforma**, con un **sistema de tipos de datos dinámico**, **administración automática de memoria** y con soporte para varios paradigmas de programación, incluyendo **programación orientada a objetos**, **programación funcional**, **programación imperativa** y **programación procedimental**.

La comunidad de programadores de Python ha establecido varios principios de diseño de programas y un conjunto de mejores prácticas. Un programa se considera **"pitónico"** si sigue estos principios y prácticas.

Python es también muy popular en el área de **procesamiento de datos geoespaciales**, en dónde se emplea como lenguaje de desarrollo de aplicaciones y como lenguaje de *scripting* en sistemas de información geográfica, sistemas administradores de bases de datos y servidores web de mapas.

## El lenguaje de programación Python

[Python](https://www.python.org/) es un lenguaje de programación de propósito general que ha alcanzado una gran popularidad en los últimos años. Fue declarado el lenguaje del año en 2020 y 2021 por el índice [Tiobe](https://www.tiobe.com/tiobe-index/) de popularidad de lenguajes de programación, debido al crecimiento de su uso en diversas áreas, entre las que destacan la [ciencia de datos](https://es.wikipedia.org/wiki/Ciencia_de_datos) y el [aprendizaje automático](https://es.wikipedia.org/wiki/Aprendizaje_autom%C3%A1tico), además de otras como desarrollo web, _scripting_ y visualización de datos, entre muchas. Esta popularidad es respaldada por otras fuentes como el índice [PYPL](http://pypl.github.io/PYPL.html) y el sitio de preguntas y respuestas para programadores [Stack Overflow](https://survey.stackoverflow.co/2024/technology#2-programming-scripting-and-markup-languages). Este último lo consideró, en 2017, el [lenguaje de programación de mayor crecimiento en los países de alto ingreso](https://stackoverflow.blog/2017/09/06/incredible-growth-python/?_ga=2.202250515.367846061.1552160385-2089845565.1546395318), como se muestra en la {numref}`figure-crecimiento-lenguajes`.

```{figure} img/growth_major_languages.png
:name: figure-crecimiento-lenguajes

Crecimiento de los principales lenguajes de programación en los países de alto ingreso. Imagen de {cite}`robinson_incredible_2017`.
```

Python también es ampliamente utilizado en enseñanza de la programación. En 2014, era el [lenguaje más empleado en cursos introductorios de programación de las principales universidades de Estados Unidos](https://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-u-s-universities/fulltext), como puede apreciarse en el gráfico de la {numref}`figure-lenguajes-universidades`.

```{figure} img/top-languajes-universities.png
:name: figure-lenguajes-universidades

Lenguajes de programación utilizados en los departamentos de ciencias de la computación de las principales universidades de Estados Unidos. Imagen de {cite}`guo_python_2014`.
```

Este uso en enseñanza se debe, entre otras razones, a que los programas en Python son más fáciles de leer y requieren menos líneas de código fuente que otros lenguajes de amplia difusión, tales como Java, C o C++.

### Historia

Python fue creado por el programador holandés [Guido van Rossum](https://gvanrossum.github.io//), quién concibió el diseño original del lenguaje a finales de la década de 1980 y dio a conocer la primera versión en 1991.

El nombre del lenguaje es un homenaje al grupo de comedia británico [Monty Python](https://es.wikipedia.org/wiki/Monty_Python). [Según van Rossum](https://www.python.org/doc/essays/foreword/), en diciembre de 1989 buscaba un proyecto de programación como "pasatiempo" durante los días cercanos a la navidad, por lo que decidió escribir un interpretador para un lenguaje de programación en el que había estado pensando recientemente. Escogió el nombre Python por encontrarse en un "humor ligeramente irreverente" y ser un gran aficionado al programa de televisión ["El circo volador de Monty Python" (_Monty Python's Flying Circus_)](https://es.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus) ({numref}`figure-monty-python`).

```{figure} img/montypython.jpg
:name: figure-monty-python

El circo volador de Monty Python. Fuente: [Internet Movie Database (IMDB)](http://www.imdb.com/title/tt0063929/).
```

La "cultura" de Python ocasionalmente hace referencia a Monty Python en tutoriales, ejemplos y otros materiales. Por ejemplo, en el [uso de _spam_, _ham_ y _eggs_ como variables metasintéticas](https://en.wikipedia.org/wiki/Metasyntactic_variable) en sustitución de las tradicionales [_foo_, _bar_ y _baz_](https://en.wikipedia.org/wiki/Foobar), en alusión al _sketch_ [Spam](https://es.wikipedia.org/wiki/Spam_(Monty_Python)) ([video del _sketch_](https://www.youtube.com/watch?v=_bW4vEo1F4E)).

### Principales características del lenguaje

La filosofía de diseño de Python enfatiza la importancia de que los programas sean fáciles de leer, de manera que los programadores puedan entender rápidamente su propósito, control de flujo y funcionamiento. Esto facilita el mantenimiento de los programas existentes y disminuye la necesidad de crear otros nuevos.

Las siguientes son otras características importantes del lenguaje Python:

- Es [interpretado](https://es.wikipedia.org/wiki/Int%C3%A9rprete_(inform%C3%A1tica)): las instrucciones se traducen una por una a [lenguaje de máquina](https://es.wikipedia.org/wiki/Lenguaje_de_m%C3%A1quina), a diferencia de los [lenguajes compilados](https://es.wikipedia.org/wiki/Compilador), que traducen de manera conjunta las instrucciones de una unidad completa (ej. un programa o una biblioteca). Los lenguajes interpretados tienden a ser más lentos que los compilados, pero también son más flexibles como entornos de desarrollo y depuración.
- Tiene un [sistema de tipos de datos dinámico](https://es.wikipedia.org/wiki/Tipado_din%C3%A1mico): las variables pueden tomar diferentes tipos de datos (ej. textuales, numéricos) durante la ejecución del programa, a diferencia de un [sistema de tipos de datos estático](https://es.wikipedia.org/wiki/Sistema_de_tipos#Tipado_est%C3%A1tico), en el que las variables solo pueden tener un tipo de datos durante la ejecución del programa. La mayoría de los lenguajes de tipos dinámicos son también lenguajes interpretados.
- Cuenta con [administración automática de memoria](https://en.wikipedia.org/wiki/Memory_management#Automated_memory_management): el interpretador se encarga de asignar y administrar la memoria de las variables, sin intervención del programador. Esto incluye un sistema de [recolección de basura](https://es.wikipedia.org/wiki/Recolector_de_basura), que libera la memoria de las variables que no están siendo utilizadas.
- Soporta varios [paradigmas de programación](https://es.wikipedia.org/wiki/Paradigma_de_programaci%C3%B3n): los paradigmas son estilos o enfoques teóricos de programación. En el caso de Python, incluye [programación orientada a objetos](https://es.wikipedia.org/wiki/Programaci%C3%B3n_orientada_a_objetos), [programación imperativa](https://es.wikipedia.org/wiki/Programaci%C3%B3n_imperativa), [programación funcional](https://es.wikipedia.org/wiki/Programaci%C3%B3n_funcional) y [programación procedimental](https://es.wikipedia.org/wiki/Programaci%C3%B3n_por_procedimientos).
- Es [multiplataforma](https://es.wikipedia.org/wiki/Multiplataforma): puede ejecutarse en los sistemas operativos más populares (ej. Windows, macOS, Linux).

### Principios de diseño

#### El Zen de Python

La filosofía de diseño de Python está resumida en una lista de 19 principios conocida como el [Zen de Python](https://www.python.org/dev/peps/pep-0020/) que guían el uso del lenguaje.

#### Guía de estilo para código Python

Los principios de diseño se reflejan en la [guía de estilo para código Python](https://www.python.org/dev/peps/pep-0008/), la cual proporciona una serie de convenciones para la escritura de programas.

#### Programas "pitónicos"

La aplicación de estos principios y el seguimiento de mejores prácticas y de [_idioms_ de programación](https://en.wikipedia.org/wiki/Programming_idiom), como los descritos en [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/), hacen que un programa se considere "pitónico" (_pythonic_). Los programadores que siguen la filosofía de Python son llamados [_pythonists_, _pythoneers_ o pythonistas](https://david.goodger.org/projects/pycon/2007/idiomatic/).

### Licenciamiento

[Python Software Foundation (PSF)](https://www.python.org/psf/) es la organización sin fines de lucro que posee los derechos de propiedad intelectual del lenguaje Python y que maneja las licencias de software libre con las que se distribuye. Su misión es _"promover, proteger y avanzar el lenguaje de programación Python, así como apoyar y facilitar el crecimiento de una comunidad diversa e internacional de programadores de Python"_.

La implementación de referencia del interpretador de Python, llamada [CPython](https://github.com/python/cpython), es software de [código abierto (_open source_)](https://es.wikipedia.org/wiki/C%C3%B3digo_abierto), lo que facilita que el desarrollo de Python sea conducido por una comunidad de programadores enlazada a través de Internet. Este modelo es seguido por la mayoría de las implementaciones del interpretador de Python. Una muestra muy representativa de este esquema de colaboración es el [Python Package Index (PyPI)](https://pypi.python.org), un repositorio para compartir componentes de software programados con Python, que a la fecha alberga más de medio millón de proyectos.

### Python 2 y Python 3

La versión 3 de Python fue liberada en 2008 y tiene diferencias en su sintaxis que la hacen incompatible con la versión 2. Desde entonces, se recomienda la migración de los programas en Python 2 a Python 3 y el uso de Python 3 para el desarrollo de nuevas aplicaciones. Ya no se brinda soporte oficial para Python 2. La PSF proporciona una [guía oficial para migrar programas de Python 2 a Python 3](https://docs.python.org/3/howto/pyporting.html).

Este curso se enfoca en Python 3. Cabe destacar que las [diferencias de importancia entre ambas versiones son realmente pocas](https://learntocodewith.me/programming/python/python-2-vs-python-3/#2018-differences-of-python2-vs-3) y un programador experimentado en el uso de Python 3 puede entender facilidad un programa en Python 2 y viceversa.

## Aplicación en datos geoespaciales

Python ha ganado una gran importancia en el área del desarrollo de aplicaciones geoespaciales debido a su popularidad, "suavidad" de la curva de aprendizaje y abundancia de recursos de educación y consulta (ej. tutoriales, libros, listas de correo, foros de discusión). Todas estas son características que, entre otras, lo hacen muy apropiado para programadores que no son especialistas en ciencias de la computación, como es el caso de muchos de los usuarios de [sistemas de información geográfica (SIG)](https://es.wikipedia.org/wiki/Sistema_de_informaci%C3%B3n_geogr%C3%A1fica) y otros tipos de software geoespacial. De hecho, muchas de estas herramientas han seleccionado a [Python como el lenguaje de preferencia para que sus usuarios amplíen o configuren la funcionalidad que ofrecen](http://www.mdpi.com/2220-9964/2/1/201). Como ejemplos, pueden mencionarse las bibliotecas [ArcPy](http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy/what-is-arcpy-.htm) para [ArcGIS](https://www.arcgis.com/), [PyQGIS](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/) para [QGIS](https://www.qgis.org/) y [PyGRASS](https://grass.osgeo.org/grass84/manuals/libpython/pygrass_index.html) para [GRASS GIS](https://grass.osgeo.org/).

En la {numref}`figure-python-gis`, puede observarse como Python es ampliamente utilizado como lenguaje de _scripting_ en software para manejo de datos geoespaciales.

```{figure} img/python-gis-software.png
:name: figure-python-gis

Uso de Python en software para manejo de datos geoespaciales. Imagen de {cite}`zambelli_pygrass_2013`.
```

## Herramientas para desarrollo

Hay una gran cantidad de herramientas disponibles para desarrollar programas en Python, incluyendo editores de código fuente, ambientes de desarrollo integrados y cuadernos de notas (*notebooks*). Entre las más usadas pueden mencionarse:

### Visual Studio Code

[Visual Studio Code (VS Code)](https://code.visualstudio.com/) es un editor de código fuente ligero y multiplataforma desarrollado por Microsoft como software libre. Es ampliamente utilizado debido a su flexibilidad, extensibilidad y rendimiento. Soporta una amplia gama de lenguajes de programación, incluyendo Python, JavaScript, C y C++, entre otros, y ofrece características como autocompletado de código, depuración integrada y control de versiones, usualmente disponibles en herramientas de desarrollo más complejas, como los [ambientes de desarrollo integrados (IDE, *Integrated Development Environment*)](https://es.wikipedia.org/wiki/Entorno_de_desarrollo_integrado).

Una de las mayores fortalezas de VS Code es su ecosistema de [extensiones](https://marketplace.visualstudio.com/VSCode), que permite a los usuarios personalizar y expandir sus capacidades según las necesidades de cada proyecto.

VS Code también permite el desarrollo de cuadernos de notas, como los que se describen en la siguiente sección.

### Jupyter Notebook y Jupyter Lab

[Jupyter Notebook](https://jupyter.org/) es una aplicación web de código abierto que permite crear y compartir documentos llamados cuadernos de notas o *notebooks* que combinan código fuente en Python (y otros lenguajes de programación) con texto narrativo en Markdown y visualizaciones como gráficos estadísticos y mapas. Es especialmente popular en el ámbito de la ciencia de datos, el análisis de datos y la investigación académica.

[JupyterLab](https://blog.jupyter.org/jupyterlab-is-ready-for-users-5a6f039b8906) es la siguiente generación de la interfaz de usuario de Jupyter Notebook y proporciona un entorno de desarrollo más flexible y poderoso. Extiende las capacidades de los Jupyter Notebooks al permitir la carga de múltiples documentos y vistas en diferentes paneles JupyterLab también ofrece un mejor soporte para extensiones y herramientas interactivas.

La interfaz de un Jupyter Notebook se muestra en la {numref}`figure-jupyter-holamundo`.

```{figure} img/jupyter-holamundo.png
:name: figure-jupyter-holamundo

Programa ["Hola Mundo"](https://es.wikipedia.org/wiki/Hola_mundo) en un Jupyter Notebook.
```

## Instalación

El interpretador de Pyhon puede obtenerse de varias formas. Una de la más usuales es en la [página de descargas de Python.org](https://www.python.org/downloads/), en donde pueden encontrarse instaladores para los diferentes sistemas operativos. Sin embargo, existen otras opciones como la que se describe en la siguiente sección.

### Con Miniconda/Anaconda

En este curso, se utilizará [Miniconda](https://docs.anaconda.com/miniconda/), una distribución libre y de código abierto de Python y de otras herramientas utilizadas en ciencia de datos. Contiene un instalador mínimo para el sistema de gestión de paquetes y entornos virtuales [conda](https://docs.conda.io). Es una versión reducida de una distribuión más amplia llamada [Anaconda](https://www.anaconda.com/). La instalación inicial de Miniconda incluye solamente conda, el interpretador de Python y unos pocos paquetes adicionales.

El administrador de paquetes conda permite el manejo de [entornos virtuales (*environments*)](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), los cuales son ambientes aislados que permiten a los usuarios y desarrolladores manejar sin conflictos diferentes versiones de paquetes, bibliotecas y dependencias para proyectos específicos.

## Ambientes de ejecución en la nube

Hay varias plataformas que ofrecen la posibilidad de ejecutar *notebooks* en la [nube](https://es.wikipedia.org/wiki/Computaci%C3%B3n_en_la_nube), como una alternativa a la ejecución en una computadora personal.

### Google Colaboratory

[Google Colaboratory](https://colab.research.google.com/) (también llamado *Colab*) ofrece un ambiente gratuito para ejecutar los *notebooks* y almacenarlos en [Google Drive](https://drive.google.com/).

### Otros

Existen otros ambientes de ejecución en la nube, como [Binder](https://mybinder.org/) y [Kaggle](https://www.kaggle.com/).

## Ejercicios

### Instalación de software

1. Instale la distribución de Python [Miniconda](../software/miniconda.md).
2. Cree un entorno virtual para el curso.
3. Instale las extensiones para Python de [VS Code](../software/vscode.md).

### Desarrollo y ejecución de programas en Python

1. Escriba un programa en Python llamado `imc.py` para calcular el [índice de masa corporal (IMC)](https://es.wikipedia.org/wiki/%C3%8Dndice_de_masa_corporal) de una persona (puede usar uno de los ejemplos vistos en el curso) y ejecútelo desde la línea de comandos de Miniconda y desde VS Code. Pruebe las herramientas de depuración de programas (*debugging*) de VS Code.
2. Escriba un cuaderno de notas para el cálculo del IMC. Agregue encabezados para el título y para secciones de entrada, procesamiento y salida. Distribuya el código fuente en esas secciones. Ejecute el cuaderno de notas en:

   a. Jupyter Notebook.  
   b. Jupyter Lab.  
   c. VS Code.

## Referencias bibliográficas

```{bibliography}
:filter: docname in docnames
```
