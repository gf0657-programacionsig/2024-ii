# Introducción a la ciencia de datos geoespaciales


## Trabajo previo

### Lecturas
Rey,	S.	J.,	Arribas-Bel,	D.,	&	Wolf,	L.	J.	(2020).	*Geographic	Data	Science	with	Python*. https://geographicdata.science/book/


## Introducción
La **ciencia de datos geoespaciales** es una especialización de la ciencia de datos que considera variables espaciales como la **localización**, la **distancia** y las [**relaciones topológicas**](https://gf0604-procesamientodatosgeograficos.github.io/2024-i/13-operaciones-datos-espaciales.html#relaciones-topol%C3%B3gicas) (ej. intersección, traslape, cobertura), las cuales usualmente no son tomadas en cuenta por la ciencia de datos convencionales. 

Adicionalmente, la ciencia de datos geoespaciales utiliza herramientas y métodos especializados, algunos de los cuales provienen de otras tecnologías de procesamiento de datos espaciales, como los [**sistemas de información geográfica (SIG)**](https://es.wikipedia.org/wiki/Sistema_de_informaci%C3%B3n_geogr%C3%A1fica). Sin embargo, la ciencia de datos geoespaciales extiende las capacidades de los SIG mediante técnicas estadísticas y computacionales más avanzadas para el análisis y la modelización. Además, puede requerir de una mayor capacidad de procesamiento y de flujos de trabajo ([*pipelines*](https://datascientest.com/es/pipeline-definicion-funcionamiento-y-uso-en-data-science)) más complejos.

El uso masivo de tecnologías como dispositivos móviles, redes sociales y sensores remotos, entre muchas otras, ha incrementado significativamente la disponibilidad de datos geoespaciales en formato digital y la conveniencia de su procesamiento mediante técnicas de ciencia de datos.


## Características de los datos geoespaciales
Toda observación tiene asociada una localización en el espacio (ej. coordenadas geográficas), la cual permite entender mejor sus relaciones con otras observaciones y que puede ser utilizada para realizar mejores inferencias y predicciones. Como lo afirmó el geógrafo estadounidense [Waldo Tobler (1930 - 2018)](https://en.wikipedia.org/wiki/Waldo_R._Tobler): 

> *Todas las cosas están relacionadas entre sí, pero las cosas cercanas están más relacionadas que las distantes* {cite}`tobler_computer_1970`. 

Por lo tanto, si se entienden apropiadamente las relaciones espaciales entre los datos, es posible desarrollar mejores modelos {cite}`rey_geographic_2020`.


## Modelos de datos geoespaciales
Los modelos de datos geoespaciales se utilizan para representar procesos geográficos en una computadora {cite}`rey_geographic_2020`. Los modelos más utilizados son el vectorial y el raster.

### Modelo vectorial
Se usa para representar objetos discretos como puntos (ej. personas, postes telefónicos), líneas (ej. ríos, caminos) y polígonos (ej. provincias, fincas) que ocupan una posición específica en el espacio y en el tiempo. Los datos vectoriales se almacenan en tablas como la que se muestra en la {numref}`figure-tabla-vectorial`. Estas tablas contienen una columna para almacenar las geometrías.

```{figure} img/tabla-vectorial.png
:name: figure-tabla-vectorial

Datos vectoriales almacenados en un `geodataframe` del paquete `geopandas` de Python. Imagen de {cite}`rey_geographic_2020`.
```

### Modelo raster
Se usa para representar superficies (ej. temperatura, precipitación, densidad de población) que, en teoría, pueden ser medidas en cualquier posición en el espacio y en el tiempo. Los datos raster se almacenan en arreglos multidimensionales (matrices, cubos) como el que se muestra en la {numref}`figure-matriz-raster`.

```{figure} img/matriz-raster.png
:name: figure-matriz-raster

Datos raster almacenados en un `Data.Array` del paquete `xarray` de Python. Imagen de {cite}`rey_geographic_2020`.
```

### Redes
Sergio Rey, Daniel Arribas-Bel y Levi Wolf {cite}`rey_geographic_2020` incluyen las redes, un conjunto de conexiones entre objetos, como otro modelo de datos, el cual puede implementarse mediante [grafos](https://es.wikipedia.org/wiki/Grafo). La {numref}`figure-grafo-red` muestra una red.

```{figure} img/grafo-red.png
:name: figure-grafo-red

Datos de red. Imagen de {cite}`rey_geographic_2020`.
```

## Herramientas de software geoespacial
El software geoespacial incluye programas SIG de escritorio (ej. QGIS, ArcGIS), programas utilitarios para la línea de comandos del sistema operativo (ej. GDAL), servidores web de mapas (ej. GeoServer, MapServer) y sistemas administradores de bases de datos (ej. PostgreSQL/PostGIS, Oracle Spatial and Graph). Muchos de estos programas utilizan bibliotecas programadas en C/C++ que han sido migradas a otros lenguajes de programación y proporcionan funcionalidades básicas para conversiones entre formatos, geoprocesamiento y conversiones entre sistemas de coordenadas. Algunas de las principales de estas bibliotecas son:

-   [Geospatial Data Abstraction Library (GDAL)](https://gdal.org/): es una biblioteca para leer y escribir datos geoespaciales en varios formatos [raster](https://gdal.org/drivers/raster/) y [vectoriales](https://gdal.org/drivers/vector/). Implementa un único [modelo abstracto de datos raster](https://gdal.org/user/raster_data_model.html) y un único [modelo abstracto de datos vectoriales](https://gdal.org/user/vector_data_model.html), lo que permite programar aplicaciones geoespaciales sin tener que ocuparse de las particularidades de cada formato que se utilice (GeoTIFF, NetCDF, ESRI Shapefile, GeoJSON, etc.). A pesar de que GDAL está programada en C/C++, cuenta con una interfaz de programación de aplicaciones (API) para varios lenguajes de programación, incluyendo [C](https://gdal.org/api/index.html#c-api), [C++](https://gdal.org/api/index.html#id3), [Python](https://gdal.org/python/index.html) y [Java](https://gdal.org/java/overview-summary.html). Además, ofrece un conjunto de [utilitarios de línea de comandos](https://gdal.org/programs/) cuyas [distribuciones binarias](https://gdal.org/download.html#binaries) están disponibles para varios sistemas operativos, incluyendo Windows, macOS y Linux.
-   [Geometry Engine, Open Source (GEOS)](https://trac.osgeo.org/geos): es una implementación en C++ de la biblioteca [JTS Topology Suite](http://www.tsusiatsoftware.net/jts/main.html) (desarrollada en Java) y que implementa un conjunto de operaciones y predicados geoespaciales (ej. unión, intersección, distancia, área).
-   [PROJ](https://proj.org/): es una biblioteca que transforma coordenadas entre diferentes CRS, incluyendo tanto proyecciones cartográficas como transformaciones geodésicas.


## Referencias bibliográficas
```{bibliography}
:filter: docname in docnames
```