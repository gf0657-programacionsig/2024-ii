# Introducción a la ciencia de datos


## Trabajo previo

### Lecturas
Çetinkaya-Rundel, Mine, & Hardin, Johanna (2021). *Chapter 1: Hello data* en *Introduction to Modern Statistics* (1st ed.). OpenIntro, Inc. https://openintro-ims.netlify.app/data-hello

Wickham, Hadley; Çetinkaya-Rundel, Mirne; & Grolemund, Garret (2023). *Introduction* en *R for Data Science: Import, Tidy, Transform, Visualize, and Model Data* (2nd ed.). O’Reilly Media. https://r4ds.hadley.nz/intro


## Introducción
Una investigación estadística se basa en **datos**. Los datos acostumbran representarse en tablas, en las cuales cada fila es una **observación** y cada columna es una **variable**. Una observación corresponde a un elemento de datos que ha sido estudiado y cada variable a una característica de ese elemento de datos. Las variables pueden ser **numéricas** o **categóricas**. Las numéricas se subdividen en **discretas** y **continuas** y las categóricas en **nominales** y **ordinales**.

La **ciencia de datos** es una disciplina que permite convertir datos “crudos” en comprensión y conocimiento. Incluye los procesos **importar**, **ordenar**, **transformar**, **visualizar**, **modelar** y **comunicar**.


## Datos
Los científicos tratan de responder preguntas mediante métodos rigurosos y observaciones cuidadosas. Estas observaciones, recopiladas de notas de campo, encuestas y experimentos, entre otras fuentes, forman la columna vertebral de una investigación estadística y se denominan **datos**. La presentación y descripción efectivas de los datos constituyen el primer paso en un análisis {cite}`cetinkaya-rundel_introduction_2021`. Esta sección introduce una estructura para organizar los datos, así como alguna terminología que se utilizará a lo largo de este curso.

### Observaciones y variables
La tabla 1 contiene 10 filas de un **conjunto de datos**. Cada fila representa una persona. En términos estadísticos, cada fila corresponde a una **observación**. Las columnas representan características de las personas. Cada columna corresponde a una **variable**.

<table border="0" cellspacing="10" class="dataframe">
  <style>
    .dataframe {
        border-spacing: 10px 10px;
    }
    .dataframe td, .dataframe th {
        padding-left: 5px;
        padding-right: 5px;
        padding-top: 2px;
        padding-bottom: 2px;
    }
  </style>
  <caption><strong>Tabla 1. Datos de personas.</strong></caption>
  <thead>
    <tr style="text-align: right;">
      <th>cedula</th>
      <th>provincia</th>
      <th>equipo</th>
      <th>peso</th>
      <th>estatura</th>
      <th>sexo</th>
      <th>cantidad_hermanos</th>
      <th>nivel_guitarra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>709880238</td>
      <td>Limón</td>
      <td>Saprissa</td>
      <td>51.0</td>
      <td>1.51</td>
      <td>desconocido</td>
      <td>0</td>
      <td>nulo</td>
    </tr>
    <tr>
      <td>400680168</td>
      <td>Heredia</td>
      <td>Herediano</td>
      <td>98.5</td>
      <td>1.87</td>
      <td>hombre</td>
      <td>1</td>
      <td>alto</td>
    </tr>
    <tr>
      <td>509210285</td>
      <td>Guanacaste</td>
      <td>Liberia</td>
      <td>91.6</td>
      <td>1.65</td>
      <td>mujer</td>
      <td>4</td>
      <td>bajo</td>
    </tr>
    <tr>
      <td>701950272</td>
      <td>Limón</td>
      <td>Liberia</td>
      <td>60.6</td>
      <td>1.68</td>
      <td>mujer</td>
      <td>1</td>
      <td>alto</td>
    </tr>
    <tr>
      <td>309880238</td>
      <td>Cartago</td>
      <td>Cartaginés</td>
      <td>59.1</td>
      <td>1.73</td>
      <td>mujer</td>
      <td>3</td>
      <td>bajo</td>
    </tr>
    <tr>
      <td>908280708</td>
      <td>Desconocida</td>
      <td>San Carlos</td>
      <td>59.2</td>
      <td>1.89</td>
      <td>hombre</td>
      <td>3</td>
      <td>bajo</td>
    </tr>
    <tr>
      <td>505580938</td>
      <td>Guanacaste</td>
      <td>Cartaginés</td>
      <td>65.2</td>
      <td>1.70</td>
      <td>mujer</td>
      <td>3</td>
      <td>alto</td>
    </tr>
    <tr>
      <td>504080488</td>
      <td>Guanacaste</td>
      <td>Sporting</td>
      <td>76.2</td>
      <td>1.76</td>
      <td>hombre</td>
      <td>3</td>
      <td>experto</td>
    </tr>
    <tr>
      <td>709950244</td>
      <td>Limón</td>
      <td>Alajuelense</td>
      <td>71.6</td>
      <td>1.80</td>
      <td>hombre</td>
      <td>4</td>
      <td>bajo</td>
    </tr>
    <tr>
      <td>206080825</td>
      <td>Alajuela</td>
      <td>Alajuelense</td>
      <td>64.6</td>
      <td>1.52</td>
      <td>hombre</td>
      <td>2</td>
      <td>bajo</td>
    </tr>
  </tbody>
</table>

### Tipos de variables
Las variables de los datos de la tabla 1 son de varios tipos, cuya jerarquía se muestra en la {numref}`figure-tipos-variables-estadisticas`.

```{figure} img/tipos-variables-estadisticas.png
:name: figure-tipos-variables-estadisticas

Tipos de variables estadísticas. Imagen de [Introduction to Modern Statistics](https://openintro-ims.netlify.app/).
```

Seguidamente, se describen estos tipos de datos de las variables.

#### Numéricas
Corresponden a números a los cuales se les pueden aplicar operaciones como suma, resta, multiplicación, división y otras similares. Las variables numéricas puden ser discretas o continuas.

##### Discretas
Toman valores específicos que se pueden contar. La variable `cantidad_hermanos` es discreta. Existe una separación clara entre sus posibles valores. Por ejemplo, es posible tener 1, 2 o 3 hermanos, pero no es posible tener 2.5 hermanos.

##### Continuas
Pueden tomar cualquier valor dentro de un intervalo o rango continuo. Estas variables se caracterizan por su capacidad para representar medidas precisas y pueden asumir un número infinito de valores, incluso dentro de un rango limitado (ej. entre 0 y 1). Las variables `peso` y `estatura` son continuas.

#### Categóricas
Las variables categóricas (también llamadas cualitativas), son aquellas que describen una característica o cualidad de una observación y clasifican las observaciones en grupos o categorías. A diferencia de las variables numéricas, que expresan cantidades numéricas, las variables categóricas expresan atributos no numéricos. Las variables categóricas pueden ser nominales u ordinales.

##### Nominales
No existe un orden inherente o jerarquía entre las categorías. Las variables `provincia`, `equipo` y `sexo` son nominales.

##### Ordinales
Hay un orden o jerarquía clara entre las categorías. La variable `nivel_guitarra` es categórica.


## Ciencia de datos
La ciencia de datos es una disciplina que permite convertir datos "crudos" en comprensión y conocimiento {cite}`wickham_r_2023`. Utiliza estadística y ciencias de la computación, entre otras disciplinas.

La {numref}`figure-modelo-ciencia-datos` ilustra el modelo de un proyecto típico de ciencia de datos, el cual incluye los procesos de importar, ordenar, transformar, visualizar, modelar y comunicar. Todos se articulan mediante **programación** de computadoras.

```{figure} img/modelo-ciencia-datos.svg
:name: figure-modelo-ciencia-datos

Modelo de ciencia de datos. Imagen de [R for Data Science](https://r4ds.had.co.nz/).
```

**Importar** los datos típicamente implica leerlos de un archivo, una base de datos o una interfaz de programación de aplicaciones (API) y cargarlos en estructuras apropiadas para este propósito en un lenguaje de programación. 

**Ordenar** u organizar los datos significa colocarlos en estructuras rectangulares de filas y columnas, similares a tablas, de manera que cada fila sea una observación y cada columna una variable.

**Transformar** los datos implica la generación de algún subconjunto de filas y columnas, la creación de nuevas variables o el cálculo de estadísticas (ej. conteos, promedios, mínimos, máximos). 

**Visualizar** los datos (en tablas, gráficos, mapas, etc.) permite encontrar patrones inesperados o formular nuevas preguntas. 

**Modelar** es crear una representación abstracta y estructurada de los datos, con el fin de facilitar su análisis y realizar predicciones.

**Comunicar** es el último paso y es una actividad crítica de cualquier proyecto de análisis de datos o de ciencia en general.


## Referencias bibliográficas
```{bibliography}
:filter: docname in docnames
```