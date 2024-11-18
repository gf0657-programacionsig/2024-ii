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

Se recomienda crear un entorno virtual. Por ejemplo:

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
Puede ver el código fuente de una aplicación Strealit de ejemplo en:

[https://github.com/gf0657-programacionsig/2024-ii-app-covid](https://github.com/gf0657-programacionsig/2024-ii-app-covid)

## Recursos de interés
- [Sitio principal](https://streamlit.io/)
- [Guía de inicio](https://docs.streamlit.io/library/get-started)
- [Documentación](https://docs.streamlit.io/)
- [Streamlit Cloud](https://streamlit.io/cloud)
- [Referencia del API](https://docs.streamlit.io/library/api-reference)
- [Galería de aplicaciones](https://streamlit.io/gallery)
