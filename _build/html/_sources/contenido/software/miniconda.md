# Miniconda

## Descripción

Miniconda es un instalador mínimo para el sistema de gestión de paquetes y entornos virtuales [conda](https://docs.conda.io). Es una versión reducida de [Anaconda](https://www.anaconda.com/) que incluye solamente conda, Python, los paquetes de los que ambos dependen y unos pocos paquetes adicionales.

## Sitio web

[Miniconda](https://docs.anaconda.com/miniconda/)

## Instalación

Descargue del sitio web el instalador correspondiente a su sistema operativo y ejecútelo. Durante el proceso de instalación, se recomienda elegir la opción **Just Me** (para que se instale en el directorio del usuario) y aceptar las otras opciones que presenta por defecto el instalador.

## Creación de un entorno virtual

Los siguientes comandos deben ejecutarse en una interfaz de comandos del sistema operativo que tenga habilitada Miniconda o Anaconda (ej. Anaconda Prompt, en Windows).

```shell
# Actualización de conda
conda update conda

# Creación de un ambiente conda llamado geopython (puede usarse cualquier otro nombre)
# con la versión 3.11 de Python
conda create --name geopython python=3.11

# Activación del ambiente
conda activate geopython

# Configuración del ambiente 
# para asegurarse de instalar todos los módulos desde el canal conda-forge
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict

# Instalación del paquete mamba (para instalaciones más rápidas)
conda install -c conda-forge mamba

# Instalación de los paquetes jupyter y jupyterlab mediante mamba
mamba install -c conda-forge jupyter jupyterlab pandas matplotlib plotly geopandas owslib shapely fiona pyproj folium

# Desactivación del ambiente (al finalizar la sesión de trabajo)
conda deactivate
```

## Instalación de paquetes en un entorno virtual

Los siguientes comandos deben ejecutarse en una interfaz de comandos del sistema operativo que tenga habilitada Miniconda o Anaconda (ej. Anaconda Prompt, en Windows).

```shell
# Activación del ambiente
conda activate geopython

# Instalación de los paquetes numpy y pandas, como ejemplo
mamba install -c conda-forge numpy pandas

# Desactivación del ambiente (al finalizar la sesión de trabajo)
conda deactivate
```

## Otros comandos de conda

```shell
# Información general sobre conda
conda info

# Ayuda general sobre los comandos de conda
conda --help

# Ayuda sobre un comando
# Sintaxis: conda <NOMBRE_PAQUETE> --help
# Ejemplo:
conda install --help

# Lista de ambientes instalados
conda env list

# Lista de paquetes instalados en un ambiente
conda list

# Almacenamiento de un ambiente en un archivo de texto
# Sintaxis: conda list --explicit > <NOMBRE_ARCHIVO>
# Ejemplo:
conda list --explicit > miambiente.txt

# Creación de un ambiente a partir de un archivo de texto
# Sintaxis: conda create --name <NOMBRE_AMBIENTE> --file <NOMBRE_ARCHIVO>
# Ejemplo:
conda create --name miambiente --file miambiente.txt

# Borrado de un ambiente y de todos sus archivos
# Sintaxis: conda env remove --name <NOMBRE_AMBIENTE> --all
# Ejemplo:
conda env remove --name miambiente --all
```

Hay una lista completa de comandos de conda en:  
[Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
