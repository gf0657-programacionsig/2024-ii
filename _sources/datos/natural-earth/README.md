# Datos de Natural Earth

## Admin 0 – Details (estados soberanos)

El archivo ZIP con un SHP comprimido debe descargarse de:  
[https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_sovereignty.zip](https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_sovereignty.zip)

```shell
# Generación de archivo CSV de países de Natural Earth
ogr2ogr \
  paises.csv \
  /vsizip/ne_10m_admin_0_sovereignty.zip/ne_10m_admin_0_sovereignty.shp \
  -sql "SELECT ADM0_ISO, NAME, CONTINENT, REGION_UN, SUBREGION, REGION_WB, \
               ECONOMY, INCOME_GRP, POP_EST, GDP_MD \
        FROM ne_10m_admin_0_sovereignty \
        WHERE ADM0_ISO != '-99'"
```
