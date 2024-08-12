# Introducción a la ciencia de datos geoespaciales


## Trabajo previo

### Lecturas
Bartomeus Lab. (2016). *A reproducible workflow*. https://www.youtube.com/watch?v=s3JldKoA0zw

FOSS4G. (2021). *FOSS4G2021—Open source for open spatial data science—Anita Graser*. https://www.youtube.com/watch?v=ZjXb53pOor0

Hwang, J. P. (2021). Building a Big Data Geographical Dashboard with Open-Source Tools. *Medium*. https://medium.com/plotly/building-a-big-data-geographical-dashboard-with-open-source-tools-c5108d7d5683

Krugman, P. (2013). Opinion | The Excel Depression. *The New York Times*. https://www.nytimes.com/2013/04/19/opinion/krugman-the-excel-depression.html

Peng, R. D. (2011). Reproducible Research in Computational Science. *Science, 334*(6060), 1226-1227. https://doi.org/10.1126/science.1213847

Rey, S. J., Arribas-Bel, D., & Wolf, L. J. (2020). *Geographic Data Science with Python*. https://geographicdata.science/book/ (Parte I)

Singleton, A. D., Spielman, S., & Brunsdon, C. (2016). Establishing a framework for Open Geographic Information science. *International Journal of Geographical Information Science, 30*(8), 1507-1521. https://doi.org/10.1080/13658816.2015.1137579

Wu, Q. (2021, octubre 25). A streamlit app for creating timelapse of annual Landsat imagery (1984–2021). *Medium*. https://giswqs.medium.com/a-streamlit-app-for-creating-timelapse-of-annual-landsat-imagery-1984-2021-3db407a8ac32


## El componente geoespacial de los datos
Una gran parte de los datos disponibles contiene algún tipo de componente geográfico o espacial[^footnote-geografico-espacial]. Este componente puede expresarse de varias formas. Por ejemplo:

- **Con nombres de lugares**: *El [sapo dorado (*Incilius periglenes*)](https://es.wikipedia.org/wiki/Incilius_periglenes) era una especie de anfibio, endémica de los bosques nubosos de altitud de Monteverde, Costa Rica.*
- **Con direcciones**: *La [sede de la Organización de las Naciones Unidas (ONU)](https://es.wikipedia.org/wiki/Sede_de_la_Organizaci%C3%B3n_de_las_Naciones_Unidas) está ubicada en la ciudad de Nueva York, Estados Unidos, en la Primera Avenida, 750.*
- **Con coordenadas**: *La cima del [Monte Everest](https://es.wikipedia.org/wiki/Monte_Everest) se localiza en las coordenadas geográficas 86°55′31″ E y 27°59′17″ N, como se muestra en la {numref}`figure-mapa-nepal-everest`.

```{figure} img/nepal-map.jpg
:name: figure-mapa-nepal-everest

Mapa de Nepal que muestra la ubicación del Monte Everest en el sistema de coordenadas geográficas. Fuente: [https://www.mapsofworld.com/](https://www.mapsofworld.com/).
```

Las coordenadas correspondientes a lugares y direcciones pueden obtenerse a través de un proceso denominado [*georreferenciación*](https://es.wikipedia.org/wiki/Georreferenciaci%C3%B3n), mediante el cual, en general, se determina la posición espacial de alguna entidad en un sistema de coordenadas. La georreferenciación puede emplearse también para obtener las coordenadas de, por ejemplo, fotografías aéreas o mapas antiguos. Es un proceso que puede resultar complejo y costoso y para el que se han desarrollado metodologías y plataformas especializadas (ej. [Chapman AD & Wieczorek JR (2020) Georeferencing Best Practices](https://doi.org/10.15468/doc-gg7h-s853), [GEOLocate](https://www.geo-locate.org/), [Nominatim](https://nominatim.openstreetmap.org/ui/search.html)).

En la actualidad, hay una gran cantidad de fuentes que generan datos georreferenciados (i.e. ubicados en un sistema de coordenadas). Entre estas pueden mencionarse las tecnologías de [observación de la Tierra (*Earth Observation*)](https://ec.europa.eu/jrc/en/research-topic/earth-observation) (ej. [imágenes satelitales](https://es.wikipedia.org/wiki/Imagen_satelital)), los dispositivos móviles y los sensores remotos, entre muchas otras.

Seguidamente, se describen dos enfoques tecnológicos para el procesamiento de datos geoespaciales: el de los sistemas de información geográfica y el de ciencia de datos geoespaciales.

## Sistemas de información geográfica
A principios de la década de 1960, el geógrafo inglés [Roger Tomlinson](https://es.wikipedia.org/wiki/Roger_Tomlinson) desarrolló en Canadá el que se considera el primer sistema de información geográfica. Se trataba del [Canada Geographic Information System (CGIS)](https://en.wikipedia.org/wiki/Canada_Geographic_Information_System) y su objetivo fue manejar los datos del inventario geográfico canadiense y su análisis para la gestión del territorio rural. De manera casi simultánea al trabajo de Tomlinson, surgieron desarrollos similares en Estados Unidos y en el Reino Unido. El surgimiento de los sistemas de información geográfica no implicó solo el surgimiento de nuevas herramientas de software, sino también el desarrollo de técnicas que hasta entonces no habían sido necesarias {cite}`olaya_sistemas_2020` como, por ejemplo, la manipulación de nuevos tipos de datos geométricos (ej. puntos, líneas, polígonos).

En general, un sistema de información geográfica (SIG) maneja datos georreferenciados y los asocia con datos convencionales (ej. textos, números), como se muestra en la {numref}`figure-mapa-qgis`.

```{figure} img/mapa-qgis.png
:name: figure-mapa-qgis

Mapa elaborado en QGIS que muestra la ubicación de los aeródromos de Costa Rica.
```

Los SIG presentan los datos en capas (*layers*). Por ejemplo, el mapa de la {numref}`figure-mapa-qgis` contiene una capa base raster (la que muestra el mar y el continente), una capa de polígonos correspondiente a las provincias de Costa Rica y una capa de puntos correspondiente a los aeródromos. A la izquierda puede apreciarse la lista de esas capas y a la derecha un cuadro con información detallada sobre uno de los aeródromos.

Los SIG de escritorio (ej. [ArcGIS Desktop](https://www.esri.com/en-us/arcgis/products/arcgis-desktop/overview), [QGIS](https://www.qgis.org/)) son herramientas con interfaces de usuario muy gráficas e intuitivas, que no requieren de conocimientos de programación de computadoras y que permiten generar cartografía de alta calidad. Sin embargo, son poco flexibles y los resultados que producen son difícilmente [reproducibles](https://es.wikipedia.org/wiki/Reproducibilidad_y_repetibilidad).

## Ciencia de datos geoespaciales
Durante la última década, el uso de SIG se ha complementado con el de [ciencia de datos](https://es.wikipedia.org/wiki/Ciencia_de_datos), lo que posibilitado enriquecer la visualización y el análisis de datos geoespaciales mediante lenguajes de programación como [Python](https://www.python.org/), [R](https://www.r-project.org/) o [JavaScript](http://www.ecma-international.org/publications-and-standards/standards/ecma-262/), entre otros.

El uso de técnicas de ciencia de datos y de otros campos relacionados (ej. [aprendizaje automatizado](https://es.wikipedia.org/wiki/Aprendizaje_autom%C3%A1tico), [*big data*](https://es.wikipedia.org/wiki/Macrodatos)) ha permitido aplicar a los datos geoespaciales técnicas y metodologías como [análisis de regresión](https://es.wikipedia.org/wiki/An%C3%A1lisis_de_la_regresi%C3%B3n) y [clasificación estadística](https://es.wikipedia.org/wiki/Clasificaci%C3%B3n_estad%C3%ADstica).

## Reproducibilidad
Una de las principales características que distingue al enfoque de ciencia de datos del enfoque de SIG es la [reproducibilidad](https://es.wikipedia.org/wiki/Reproducibilidad_y_repetibilidad). En general, la reproducibilidad es la capacidad de un ensayo o experimento de ser reproducido por otros. Más formalmente, en investigación cuantitativa, un análisis se considera reproducible si *"el código fuente y los datos utilizados por un investigador para llegar a un resultado están disponibles y son suficientes para que otro investigador, trabajando de manera independiente, pueda llegar al mismo resultado"* {cite}`gandrud_reproducible_2020`.

La reproducibilidad, junto con la [falsabilidad](https://es.wikipedia.org/wiki/Falsabilidad), es uno de los pilares del [método científico](https://es.wikipedia.org/wiki/M%C3%A9todo_cient%C3%ADfico). Sin embargo, en años recientes, se ha generado una creciente preocupación debido a que muchos estudios científicos publicados fallan las pruebas de reproducibilidad (véase, por ejemplo, [*The Excel Depression*, de Paul Krugman](https://www.nytimes.com/2013/04/19/opinion/krugman-the-excel-depression.html)), dando lugar a una [crisis de reproducibilidad o replicabilidad](https://es.wikipedia.org/wiki/Crisis_de_replicaci%C3%B3n) en varias ciencias.

El concepto de reproducibilidad es cada vez más importante debido, entre otras razones, al aumento exponencial de datos disponibles y a la aplicación de la programación de computadoras, para procesar estos datos, por parte de especialistas de muchas disciplinas.

Alex Singleton y otros autores {cite}`singleton_establishing_2016` han identificado los siguientes retos para la reproducibilidad en ciencia de datos geoespaciales:

1. Los datos deben ser de dominio público y estar disponibles para los investigadores.
2. El software utilizado debe ser de código abierto (*open source*) y estar disponible para ser revisado.
3. Siempre que sea posible, los [flujos de trabajo](https://es.wikipedia.org/wiki/Flujo_de_trabajo) deben ser públicos y con enlaces a los datos, software y métodos de análisis, junto con la documentación necesaria.
4. El proceso de [revisión por pares (*peer review process*)](https://es.wikipedia.org/wiki/Revisi%C3%B3n_por_pares) y la publicación académica deben requerir la presentación de un modelo de flujo de trabajo e idealmente la disponibilidad de los materiales necesarios para la replicación.
5. En los casos en los que la reproducibilidad total no sea posible (ej. datos sensibles), los investigadores deben esforzarse por incluir todos los aspectos que puedan de un marco de trabajo abierto.

En general, el estándar mínimo de reproducibilidad requiere que los datos y el código fuente estén disponibles para otros investigadores {cite}`peng_reproducible_2011`. Sin embargo, dependiendo de las circunstancias y recursos disponibles, existe todo un espectro de posibilidades, que se ilustra en la figura {numref}`figure-espectro-reproducibilidad`.

```{figure} img/espectro-reproducibilidad.png
:name: figure-espectro-reproducibilidad

Espectro de reproducibilidad. Fuente: [Anita Graser](https://www.youtube.com/watch?v=ZjXb53pOor0), con base en [(Peng, 2001)](https://doi.org/10.1126/science.1213847).
```

### Herramientas para facilitar la reproducibilidad
En esta sección se destacan dos tipos de herramientas que en la actualidad se consideran esenciales para apoyar la reproducibilidad de una investigación: los lenguajes de marcado y los sistemas de control de versiones.

La documentación es vital durante todo el ciclo de vida de una investigación reproducible. Para documentar, se recomienda utilizar mecanismos estandarizados y abiertos como el [lenguaje de marcado de hipertexto (HTML, en inglés, *HyperText Markup Language*)](https://es.wikipedia.org/wiki/HTML) o [Markdown](https://en.wikipedia.org/wiki/Markdown), con los cuales pueden crearse documentos mediante editores de texto simples (i.e. no se requiere de software propietario), y exportables a varios formatos (ej. [LaTeX](https://es.wikipedia.org/wiki/LaTeX), [PDF](https://es.wikipedia.org/wiki/PDF)).

Para dar mantenimiento, tanto al código fuente como a la documentación, es necesario un sistema de [control de versiones](https://es.wikipedia.org/wiki/Control_de_versiones) como [Git](https://es.wikipedia.org/wiki/Git), el cual permite llevar el registro de los cambios en archivos y también facilita el trabajo colaborativo al reunir las modificaciones hechas por varias personas. Git es usado en varias plataformas que comparten código fuente (ej. [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/)) y que ofrecen servicios relacionados, como hospedaje de sitios web.

## Referencias bibliográficas
```{bibliography}
:filter: docname in docnames
```

[^footnote-geografico-espacial]: El adjetivo *geográfico* se refiere a la superficie de la Tierra. Así, por ejemplo, las *coordenadas geográficas* se utilizan para ubicar cualquier punto en la superficie terrestre. El término *espacial* se emplea para referirse a cualquier espacio, no siempre localizable en el planeta Tierra. En muchas ocasiones, ambas palabras son intercambiables. Por ejemplo, muchos de los métodos utilizados para analizar datos geográficos pueden aplicarse también en espacios no geográficos como, por ejemplo, otros planetas, el cosmos, el cuerpo humano (ej. con radiografías) o secuencias genómicas. En los últimos años, se ha incrementado el uso del término *geoespacial*, el cual se eligió para el nombre de este curso, como una forma de referirse al subconjunto del espacio correspondiente a la superficie de la Tierra {cite}`longley_geographic_2005`.
