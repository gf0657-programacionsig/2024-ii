# Introducción a la programación de computadoras


## Trabajo previo

### Lecturas
Downey, Allen B. (2024). *Chapter 1: Programming as a way of thinking* en *Think Python: How to Think Like a Computer Scientist* (3rd ed.). O’Reilly Media. https://allendowney.github.io/ThinkPython/chap01.html

Severance, D. C. R. (2016). *Chapter 1: Why should you learn to write programs?* en *Python for Everybody: Exploring Data in Python 3* (S. Blumenberg & E. Hauser, Eds.). CreateSpace Independent Publishing Platform. https://www.py4e.com/html3/


## Introducción
Una **computadora** es una máquina que ejecuta automáticamente secuencias de **instrucciones** tales como cálculos aritméticos y operaciones lógicas, entre otras. Un conjunto de instrucciones orientado a la resolución de un problema específico mediante una computadora se denomina **programa**. La programabilidad de las computadoras permite que su funcionamiento pueda modificarse sin alterar sus componentes físicos, lo que las hace mucho más versátiles que otros tipos de máquinas y posibilita que ayuden a resolver una gran variedad de problemas.

Las computadoras se programan mediante lenguajes formales denominados **lenguajes de programación**. En este capítulo, se describe el papel de los lenguajes de programación y el modelo **Entrada - Procesamiento - Salida** en el que se basa la estructura de los programas. También se detallan los componentes principales de la **arquitectura de computadoras** más popular en la actualidad. Por último se presenta el concepto de **pensamiento computacional**, un enfoque para la resolución de problemas basado en conceptos y métodos de las ciencias de la computación.

## Lenguajes para programar computadoras
Las computadoras pueden programarse mediante lenguajes de varios niveles. En esta sección, se describen el lenguaje de máquina, el más cercano al hardware de la computadora, y los lenguajes de programación, los cuales abstraen detalles técnicos y de hardware para lograr que la programación sea más intuitiva, más rápida y menos propensa a errores.

### Lenguajes de máquina
Las computadoras modernas son electrónicas y utilizan [circuitos integrados](https://es.wikipedia.org/wiki/Circuito_integrado) para procesar y almacenar información en forma de señales eléctricas. Esta representación de la información se basa en un [sistema binario](https://es.wikipedia.org/wiki/Sistema_binario) (de dos estados): 0 (voltaje bajo) y 1 (voltaje alto).

En el nivel más básico, las computadoras pueden programarse introduciendo directamente combinaciones de unos y ceros, conocidas como [lenguaje de máquina](https://es.wikipedia.org/wiki/Lenguaje_de_m%C3%A1quina) en la [Unidad Central de Procesamiento (CPU)](https://es.wikipedia.org/wiki/Unidad_central_de_procesamiento), el componente de hardware encargado de ejecutar las instrucciones.

Por ejemplo, la {numref}`figure-helloworld-lenguajemaquina` muestra el programa [Hola mundo (*Hello World*)](https://es.wikipedia.org/wiki/Hola_mundo) en lenguaje de máquina. Este programa simplemente imprime la hilera de texto “Hola mundo” en la pantalla. Suele ser usado como introducción al estudio de la programación de computadoras.

```{figure} img/helloworld-lenguajemaquina.jpeg
:name: figure-helloworld-lenguajemaquina

Lenguaje de máquina correspondiente a la implementación del programa "Hola mundo" en el lenguaje [C](https://es.wikipedia.org/wiki/C_(lenguaje_de_programaci%C3%B3n)) (mostrado abajo). Imagen de [Tanveer Salim](https://www.quora.com/What-does-a-machine-language-code-look-like).
```

```c
/* PROGRAMA "Hola mundo" EN LENGUAJE C */

int main void()
{
  printf("hello, world\n");
  return 0;
}
```

Internamente, el lenguaje de máquina ejecuta un conjunto de instrucciones muy básicas como, por ejemplo:

- Sumar dos números.
- Comprobar si un número es igual a cero.
- Copiar datos de una sección a otra de la memoria de la computadora.

Los lenguajes de máquina son específicos para cada tipo de CPU. Así, por ejemplo, el lenguaje de máquina de un procesador Intel, uno de los más usados en computadoras personales, es diferente al lenguaje de máquina de un procesador PowerPC, utilizado tanto en computadoras personales (como antiguas Macintosh), como en consolas de videojuegos y sistemas incrustados (ej. en dispositivos electrónicos).

### Lenguajes de programación
Debido a que el lenguaje de máquina es poco amigable para las personas, actualmente es más común utilizar [lenguajes de programación](https://es.wikipedia.org/wiki/Lenguaje_de_programaci%C3%B3n) para resolver problemas mediante computadoras. Los lenguajes de programación consisten de instrucciones compuestas por palabras y expresiones similares a las de los lenguajes humanos como, por lo general, el idioma inglés. 

Las instrucciones de los lenguajes de programación deben ser traducidas al lenguaje de máquina para que puedan ser ejecutados por la computadora. Esta traducción se realiza mediante programas llamados [compiladores](https://es.wikipedia.org/wiki/Compilador) (para lenguajes compilados como C o C++) o [interpretadores](https://es.wikipedia.org/wiki/Int%C3%A9rprete_(inform%C3%A1tica)) (para lenguajes interpretados como Python). Mientras que los lenguajes de máquina son específicos para cada CPU, los lenguajes de programación pueden ser portátiles y ser ejecutados en diferentes plataformas, con el compilador o interpretador adecuado.

Como ejemplo, considere problema del cálculo del [índice de masa corporal (IMC)](https://es.wikipedia.org/wiki/%C3%8Dndice_de_masa_corporal). El IMC indica si una persona tiene una masa (peso) saludable en relación con su estatura. Se obtiene mediante la fórmula: 

$$
imc = \frac{masa}{estatura^2}
$$

El resultado se interpreta de la siguiente manera:

- IMC menor que 18.5: Peso bajo.
- IMC mayor o igual que 18.5 y menor que 25: Peso normal.
- IMC mayor o igual que 25: Sobrepeso.

El siguiente programa en el lenguaje [Python](https://es.wikipedia.org/wiki/Python) calcula e interpreta el IMC de una persona.

```python
# CÁLCULO E INTERPRETACIÓN DEL IMC DE UNA PERSONA


# ENTRADA

# Datos de masa (kg) y estatura (m) de una persona
masa = 65
estatura = 1.7


# PROCESAMIENTO

# Cálculo del IMC
imc = masa / estatura**2

# Interpretación del IMC
if (imc < 18.5):
  interpretacion_imc = "Peso bajo"
elif (imc < 25):
  interpretacion_imc = "Peso normal"
else:
  interpretacion_imc = "Sobrepeso"


# SALIDA

# Impresión de los resultados
print("El valor del IMC es:", imc)
print("Corresponde a:", interpretacion_imc)
```

A manera de ejercicio, puede escribir y ejecutar el programa anterior en una [consola de Python](https://www.mycompiler.io/new/python). Modifique los datos de entrada de masa y estatura y observe los cambios en los resultados.

En el ejemplo anterior puede observarse como el programa sigue un modelo conocido como Entrada - Procesamiento - Salida, el cual se describe en detalle en la sección siguiente.


## Modelo Entrada - Procesamiento - Salida
Las computadoras trabajan con un modelo de "Entrada - Procesamiento - Salida": reciben datos de entrada (ej. números), los procesan (ej. realizan cálculos aritméticos) y generan salidas (resultados de los cálculos).

El modelo de "Entrada - Procesamiento - Salida" es un concepto fundamental en análisis de sistemas de información y desarrollo de programas. Su esquema se presenta en la {numref}`figure-entrada-procesamiento-salida`.

```{figure} img/entrada-procesamiento-salida.png
:name: figure-entrada-procesamiento-salida

Modelo Entrada - Procesamiento - Salida.
```

- La **entrada** se refiere a los datos que se introducen en un sistema o programa para ser procesados. Pueden ingresarse a través de diversas fuentes, tales como teclados, ratones, cámaras, sensores, archivos y servicios web, entre otros.
- El **procesamiento** es el conjunto de instrucciones que generan salidas a partir de las entradas. Estas intrucciones pueden incluir cálculos matemáticos, operaciones lógicas y operaciones de control, entre muchas posibilidades.
- Por último, la **salida** es el resultado del procesamiento (ej. el resultado de cálculos aritméticos).


## Arquitectura de computadoras
La [arquitectura de computadoras](https://es.wikipedia.org/wiki/Arquitectura_de_computadoras) es un área de estudio enfocada en el diseño de los componentes principales de un sistema informático. La arquitectura de las computadoras modernas es el resultado de un proceso evolutivo que ha tomado varios siglos. En esta sección se describen algunos de los principales logros alcanzados durante este proceso y se finaliza con la arquitectura de von Neumann, la más utilizada en la actualidad.

### Evolución histórica

#### Calculadoras mecánicas
En el siglo XVII, matemáticos como el francés [Blaise Pascal (1623-1662)](https://es.wikipedia.org/wiki/Blaise_Pascal) y el alemán [Gottfried Leibniz (1646-1716)](https://es.wikipedia.org/wiki/Gottfried_Leibniz) construyeron calculadoras mecánicas [calculadoras mecánicas](https://es.wikipedia.org/wiki/Calculadora_mec%C3%A1nica) capaces de sumar, restar, multiplicar y dividir. Una réplica de la máquina de Leibniz se muestra en la {numref}`figure-maquina-leibniz`.

```{figure} img/maquina-leibniz.jpg
:name: figure-maquina-leibniz

Réplica de la *Stepped Reckoner*, en el Museo Technische Sammlungen, en Dresden, Alemania. Imagen compartida a través de [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Leibnitzrechenmaschine.jpg).
```

Los derivados de las calculadoras mecánicas creadas por Pascal y Leibniz continuaron siendo producidos durante tres siglos, hasta que a principios de los años 1970 sus equivalentes electrónicos finalmente llegaron a ser fácilmente disponibles y baratos.

#### La máquina analítica de Babbage
En 1837, el matemático inglés [Charles Babbage (1791-1871)](https://es.wikipedia.org/wiki/Charles_Babbage) inició el diseño de la [máquina analítica](https://es.wikipedia.org/wiki/M%C3%A1quina_anal%C3%ADtica), la cual se muestra en la {numref}`figure-maquina-analitica`.

```{figure} img/maquina-analitica.jpg
:name: figure-maquina-analitica

Máquina analítica de Babbage, expuesta en el Museo de Ciencias de Londres. Imagen compartida a través de [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:AnalyticalMachine_Babbage_London.jpg).
```

Esta máquina estaba diseñada para realizar cálculos matemáticos de manera automática a través de una serie de instrucciones introducidas por medio de un sistema de [tarjetas perforadas](https://es.wikipedia.org/wiki/Tarjeta_perforada), el cual estaba basado en el [telar de Jacquard](https://es.wikipedia.org/wiki/Telar_de_Jacquard), un​ mecanismo ya utilizado en esa época para controlar equipos mecánicos. Además, su diseño incluía algunos componentes de una computadora moderna, incluyendo una "unidad de memoria" y una "unidad de procesamiento". La máquina analítica nunca se terminó de construir, debido a limitaciones tecnológicas y financieras.

El trabajo de Babbage se enriqueció con la contribución de la también matemática inglesa [Ada Lovelace (1815-1852)](https://es.wikipedia.org/wiki/Ada_Lovelace). Lovelace identificó el potencial que tenía la máquina analítica más allá del procesamiento numérico y que podría usarse para crear cualquier tipo de contenido, incluyendo música y otras formas de arte, anticipando así las capacidades multifuncionales de las computadoras modernas.

#### La máquina de Turing
En 1936, el matemático inglés [Alan Turing (1912-1954)](https://es.wikipedia.org/wiki/Alan_Turing) propuso un dispositivo teórico, conocido en la actualidad como [máquina de Turing](https://es.wikipedia.org/wiki/M%C3%A1quina_de_Turing), que manipula símbolos de una cinta de acuerdo con una tabla de reglas. La máquina de Turing se ilustra en la {numref}`figure-maquina-turing`.

```{figure} img/maquina-turing.png
:name: figure-maquina-turing

Representación artística de una máquina de Turing. Imagen de Schadel [compartida a través de Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Turing_Machine.png).
```

La máquina de Turing simula el funcionamiento de un [algoritmo](https://es.wikipedia.org/wiki/Algoritmo) y los conceptos de entrada, procesamiento y salida. Funciona como una base teórica para entender qué puede y qué no puede ser computado, y ha influido en el diseño y teoría de las computadoras y lenguajes de programación modernos.

#### Computadoras de la II Guerra Mundial
Con base en las ideas de Turing, las computadoras [Bombe](https://es.wikipedia.org/wiki/Bombe) y [Colossus](https://es.wikipedia.org/wiki/Colossus) fueron construídas durante la II Guerra Mundial (1939-1945) en el Reino Unido, para descifrar mensajes codificados. A pesar de que se consideran de las primeras computadoras digitales electrónicas programables, su programación se realizaba a través de componentes de *hardware*, como interruptores y enchufes, y no con un [programa almacenado](https://es.wikipedia.org/wiki/Computador_de_programa_almacenado).

También durante la II Guerra Mundial, el ejército de Estados Unidos de América construyó [ENIAC (Electronic Numerical Integrator and Computer)](https://es.wikipedia.org/wiki/ENIAC) para calcular tablas de tiro de artillería. Es considerada por algunos como la primera computadora programable digital de propósito general. Era capaz de seguir el modelo de la máquina de Turing, por lo que era [Turing-completa](https://es.wikipedia.org/wiki/Turing_completo). ENIAC se muestra en la {numref}`figure-eniac`.

```{figure} img/eniac.jpg
:name: figure-eniac

ENIAC, siendo programada por Glen Beck y Betty Snyder. Imagen del Ejército de Estados Unidos compartida a través de [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Eniac.jpg).
```

### Arquitectura de von Neumann
En 1945, el matemático húngaro-estadounidense [John von Neumann (1903-1957)](https://es.wikipedia.org/wiki/John_von_Neumann) propuso un concepto conocido como [programa almacenado](https://es.wikipedia.org/wiki/Computador_de_programa_almacenado), en el cual los datos y los programas se almacenan en una estructura llamada memoria, separada de los componentes físicos que ejecutan las instrucciones. Este modelo permite que las computadoras sean más fáciles de reprogramar y es conocido actualmente como [arquitectura de von Neumann](https://es.wikipedia.org/wiki/Arquitectura_de_Von_Neumann). La arquitectura de von Neumann se ilustra en la {numref}`figure-arquitectura-vonneumann`.

```{figure} img/arquitectura-vonneumann.jpg
:name: figure-arquitectura-vonneumann

Diagrama de la arquitectura de von Neumann. Imagen de David Strigoi compartida a través de [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Arquitecturaneumann.jpg).
```

#### Componentes de la arquitectura de von Neumann

##### Memoria principal
Almacena las instrucciones de los programas y los datos que utilizan estos programas. Es común denominarla como RAM (*Random Access Memory*, Memoria de Acceso Aleatorio), lo que significa que toma el mismo tiempo acceder a cualquier posición de la memoria. Cada posición de memoria tiene una dirección a la que se hace referencia cuando se desea leer o escribir.

##### Unidad Central de Procesamiento
También se le conoce como CPU (*Central Processing Unit*). Ejecuta las instrucciones de los programas en lenguaje de máquina. Está compuesta por dos partes:

- **Unidad de Control**: determina cuál es la siguiente instrucción a ejecutar. Contiene memorias temporales de alta velocidad y poca capacidad llamadas registros, para almacenar los operandos y el resultado de las instrucciones.
- **Unidad de Aritmética y Lógica o ALU (*Arithmetic and Logic Unit*)**: ejecuta las operaciones aritméticas y lógicas.

##### Sistemas de entrada y salida
Permiten que la computadora interactúe con el usuario y, en general, con el mundo exterior. Algunos ejemplos son el teclado y el ratón, como sistemas de entrada, y la pantalla y la impresora, como sistemas de salida.


## Aprendiendo a pensar como un programador
Las computadoras son ampliamente utilizadas en la actualidad, debido a su capacidad para ayudar a resolver problemas. Sin embargo, el problema debe expresarse de forma tal que pueda ser "entendido" por una computadora, mediante un lenguaje de programación, como se ilustra en la {numref}`figure-resolucion-problemas-computadoras`. 

```{figure} img/resolucion-problemas-computadoras.png
:name: figure-resolucion-problemas-computadoras

Resolución de problemas mediante computadoras.
```

### Lenguajes formales y naturales
Los lenguajes de programación, al igual que, por ejemplo, las notaciones lógicas y matemáticas, son [lenguajes formales](https://es.wikipedia.org/wiki/Lenguaje_formal). Fueron diseñados para aplicaciones específicas, de forma contraria a los [lenguajes naturales](https://es.wikipedia.org/wiki/Lengua_natural), que son los que usan las personas para comunicarse (ej. español, inglés, alemán) y que evolucionaron espontáneamente.

Aunque los lenguajes formales y los naturales tienen algumas características en común, también tienen diferencias importantes {cite}`downey_think_2024`:

- **Ambigüedad**: Los lenguajes naturales tienen mucha ambigüedad. Una misma palabra u oración pueden tener varios significados diferentes, dependiendo del contexto. Por su parte, los lenguajes formales están diseñados para tener poca o ninguna ambigüedad: una instrucción o expresión tiene un único significado, independientemente del contexto.
- **Redundancia**: Para lidiar con la ambigüedad y reducir las confusiones, los lenguajes naturales usan redundancia: una idea se expresa de varias maneras, lo que puede implicar el uso de muchas palabras. Los lenguajes formales tienden a ser menos redundantes y más concisos.
- **Literalidad**: Los lenguajes naturales utilizan muchas metáforas, símiles y otras formas expresivas de emplear las palabras que resultan diferentes de su uso habitual (ej. [figuras literarias](https://es.wikipedia.org/wiki/Figura_literaria)). Por el contrario, las expresiones de los lenguajes formales tienen un significado literal.

Debido a que las personas crecemos hablando lenguajes naturales, puede resultar difícil adaptarse a los lenguajes formales. Los lenguajes formales son más "densos" que los lenguajes naturales, por lo que lleva más tiempo leerlos. Además, la estructura es importante, por lo que no siempre es mejor leer de arriba hacia abajo y de izquierda a derecha, como en muchos lenguajes naturales. Finalmente, los detalles son de suma importancia. Pequeños errores en la ortografía y la puntuación, que en los lenguajes naturales pueden pasar desapercibidos, pueden hacer una gran diferencia en un lenguaje formal {cite}`downey_think_2024`.

### Pensamiento computacional
Por estas diferencias entre los lenguajes naturales y los lenguajes formales, aprender a programar implica aprender a pensar de una manera diferente, la cual combina algunas de las mejores prácticas de las matemáticas, las ingenierías y las ciencias {cite}`downey_think_2024`:

- Como en matemáticas, los programadores utilizan lenguajes formales para representar ideas.
- Al igual que un ingeniero, un programador debe diseñar e implementar componentes para integrarlos en sistemas y evaluar las ventajas y desventajas de las diferentes opciones.
- Como un científico, un programador observa el funcionamiento de sistemas complejos, formula hipótesis y evalúa modelos predictivos.

El [pensamiento computacional](https://es.wikipedia.org/wiki/Pensamiento_computacional) es un enfoque para la resolución de problemas basado en conceptos y métodos de las ciencias de la computación. Puede ser aplicado en muchas áreas, no solo en computación. Se considera una de las destrezas fundamentales del siglo XXI {cite}`wing_computational_2006`.

#### Conceptos fundamentales del pensamiento computacional
El pensamiento computacional consta de cuatro pilares o conceptos fundamentales: descomposición, reconocimiento de patrones, abstracción y algoritmos.

#### Descomposición
Consiste en la división de un problema en subproblemas más pequeños. La idea es que el problema total, de problema de mayor complejidad, se simplifique en problemas más fáciles de resolver.

Ejemplos:
- División de un documento en secciones.
- [Estructuración de un programa en bloques o subrutinas](https://es.wikipedia.org/wiki/Programaci%C3%B3n_estructurada).

#### Reconocimiento de patrones
Es la búsqueda de similitudes de un problema a resolver, con problemas ya resueltos.

"*Cada patrón describe un problema que ocurre infinidad de veces en nuestro entorno, así como la solución al mismo, de tal modo que podemos utilizar esta solución un millón de veces más adelante sin tener que volver a pensarla otra vez.*" (Christopher Alexander, 1977).

Ejemplos:
- [Patrones de diseño arquitectónico](https://laptrinhx.com/a-pattern-language-3372046788/)
- [Patrones de diseño de software](https://en.wikipedia.org/wiki/Design_Patterns)
- [*Idioms* de programación](https://en.wikipedia.org/wiki/Programming_idiom)

#### Abstracción
Se refiere a la identificación de la información que se necesita y filtrado de la que no se necesita para resolver un problema.

Ejemplos:
- Selección de atributos a incluir en una base de datos.

#### Algoritmos
Es la descripción, paso por paso, de la solución a un problema.

Ejemplos:
- [Algoritmos de ordenamiento](https://es.wikipedia.org/wiki/Algoritmo_de_ordenamiento)
- [Algoritmos de búsqueda](https://es.wikipedia.org/wiki/Algoritmo_de_b%C3%BAsqueda)

## Práctica de programación
[Scratch](https://scratch.mit.edu/) es un lenguaje de programación orientado a educación. Su nombre proviene de la palabra [*scratching*](https://en.wikipedia.org/wiki/Scratching). Fue desarrollado en 2003 por el [MIT Media Lab](https://www.media.mit.edu/) y es administrado por la Fundación Scratch, una organización sin fines de lucro que lo facilita de manera gratuita. Es software libre distribuido mediante licencia [GPLv2](https://es.wikipedia.org/wiki/GNU_General_Public_License).

- Considere el dibujo que se muestra en la {numref}`figure-casa`.

```{figure} img/casa.png
:name: figure-casa

Casa dibujada con Scratch.
```

- Ingrese al sitio web de [Scratch](https://scratch.mit.edu/) y estudie la intefaz del ambiente de desarrollo. Puede buscar información adicional en otros sitios (ej. [Scratch Tutorial for Beginners - Make a Flappy Bird Game](https://www.youtube.com/watch?v=x14G4DCk4nY), [CS50 2021 in HDR - Lecture 0 - Scratch](https://www.youtube.com/watch?v=1tnj3UCkuxU)). Revise ejemplos y proyectos de otras personas para saber qué puede hacer con Scratch.

- Utilizando los cuatro principios fundamentales del pensamiento computacional, desarrolle un algoritmo para dibujar la casa de la figura anterior. Considere las siguientes preguntas orientadoras:

  - ¿Cómo puede dividirse el problema?
  - ¿Qué patrones observa (formas, tamaños, etc.)?
  - ¿Qué información se necesita para hacer los dibujos (ej. medidas)?
  - ¿Qué nivel de detalle requiere el algoritmo?
  
- Implemente en un programa en Scratch el algoritmo que desarrolló.

Algunas sugerencias:

- Procure que el código fuente de sus programas sea ordenado y legible.
- Reutilice el código fuente mediante bloques, funciones y otros mecanismos.
- Use identificadores (ej. nombres de variables, nombres de bloques o funciones) significativos.
- Incluya comentarios en el código fuente de sus programas y también escriba documentación externa.

## Referencias bibliográficas
```{bibliography}
:filter: docname in docnames
```