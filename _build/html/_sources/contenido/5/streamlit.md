# Streamlit: marco de trabajo para desarrollo de aplicaciones web de ciencia de datos y aprendizaje automatizado

## Introducción

[Streamlit](https://streamlit.io/) es un marco de trabajo (*framework*) para el desarrollo de aplicaciones web basadas en el lenguaje de programación Python. El desarrollo en Streamlit no requiere de conocimientos de tecnologías web como HTML, CSS o JavaScript.

La plataforma [Streamlit Cloud](https://streamlit.io/cloud) permite compartir y publicar aplicaciones Streamlit, conjuntamente con el mantenimiento del código fuente en [GitHub](https://github.com/). Las aplicaciones Streamlit también pueden ser puestas en producción en otras plataformas, como [Heroku](https://www.heroku.com/) y [AWS](https://aws.amazon.com/).

## Instalación

Puede instalarse mediante pip, conda o mamba:

```shell
# Con pip
pip install streamlit

# Con conda
conda install -c conda-forge streamlit

# Con mamba
mamba install -c conda-forge streamlit
```

Se recomienda crear un entorno virtual con Streamlit y otras bibliotecas requeridas. El siguiente bloque de código contiene los comandos necesarios para crear un ambiente conda para desarrollo de aplicaciones geoespaciales.

```shell
# Actualización de Conda
conda update conda

# Borrado del ambiente (si es que existe)
# conda remove -n streamlit --all

# Creación del ambiente
conda create -n streamlit

# Activación del ambiente
conda activate streamlit

# Configuración del ambiente
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict

# Instalación de mamba
conda install -c conda-forge mamba

# Instalación de módulos
mamba install -c conda-forge python=3.12 pandas altair plotly geopandas leafmap streamlit streamlit-folium

# Desactivación del ambiente
conda deactivate
```

## Aplicación de ejemplo

Se proporciona el código fuente de una aplicación Streamlit de ejemplo en el repositorio GitHub:

[https://github.com/gf0657-programacionsig/2024-ii-app-covid](https://github.com/gf0657-programacionsig/2024-ii-app-covid)

Esta aplicación despliega un [tablero de control](https://es.wikipedia.org/wiki/Cuadro_de_mando) (también llamado cuadro de mando o *dashboard*) con datos de la pandemia de CODIV-19 compartidos por [Our World in Data](https://ourworldindata.org/).

### Ejecución en la computadora local

Para ejecutar la aplicación en su computadora, clone o descargue el repositorio con el código fuente y desde la línea de comandos del sistema operativo ingrese al directorio y ejecute:

```bash
# Ejecución de la aplicación Streamlit
streamlit run app.py
```

Este comando inicializa un servidor web de desarrollo y abre la aplicación Streamlit.

### Publicación en Streamlit Cloud

Para publicar una aplicación en Streamlit Cloud, primero debe crear un archivo llamado `requirements.txt` con la lista de las bibliotecas que usa la aplicación. Por ejemplo:

```
streamlit
pandas
plotly
geopandas
folium
streamlit-folium
branca
```

Luego, debe incluir la aplicación, y los archivos asociados (ej. datos locales), en un repositorio en GitHub.

Por último, debe ingresar a [Streamlit Cloud](https://streamlit.io/cloud) y crear una cuenta gratuita (puede usar su cuenta de GitHub). Ahí debe seleccionar el repositorio de GitHub en el que se encuentra la aplicación y publicarla.

La aplicación sobre COVID-19 está disponible en:
[https://2024-ii-app-covid.streamlit.app/](https://2024-ii-app-covid.streamlit.app/)

## Recursos de interés

- [Sitio principal](https://streamlit.io/)
- [Guía de inicio](https://docs.streamlit.io/library/get-started)
- [Documentación](https://docs.streamlit.io/)
- [Streamlit Cloud](https://streamlit.io/cloud)
- [Referencia del API](https://docs.streamlit.io/library/api-reference)
- [Galería de aplicaciones](https://streamlit.io/gallery)
