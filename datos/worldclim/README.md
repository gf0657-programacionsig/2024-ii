# Datos de WorldClim

## Altitud y variables climáticas de Costa Rica

### Altitud

```bash
# Descargar archivo ZIP con datos de altitud
wget \
    "https://geodata.ucdavis.edu/climate/worldclim/2_1/base/wc2.1_30s_elev.zip" \
    -O "wc2.1_30s_elev.zip"

# Extraer el archivo GeoTIFF de altitud
unzip wc2.1_30s_elev.zip wc2.1_30s_elev.tif

# Descargar capa de provincias de Costa Rica y fundirla en un único polígono
ogr2ogr \
    -makevalid \
    -t_srs EPSG:4326 \
    -dialect sqlite \
    -sql "SELECT ST_Union(SHAPE) AS geometry FROM \"IGN_5_CO:limiteprovincial_5k\"" \
    -nln costarica \
    "costarica.gpkg" \
    WFS:"https://geos.snitcr.go.cr/be/IGN_5_CO/wfs" "IGN_5_CO:limiteprovincial_5k"

# Recortar el raster de altitud con el contorno de Costa Rica
gdalwarp \
    -t_srs EPSG:4326 \
    -cutline "costarica.gpkg" \
    -crop_to_cutline \
    "wc2.1_30s_elev.tif" \
    "altitud.tif"

# Borrar archivos temporales
rm wc2.1_30s_elev.zip
rm wc2.1_30s_elev.tif
rm costarica.gpkg*

```

### Temperatura

```bash
# Descargar archivo ZIP con datos de variables bioclimáticas
wget \
    "https://geodata.ucdavis.edu/climate/worldclim/2_1/base/wc2.1_30s_bio.zip" \
    -O "wc2.1_30s_bio.zip"

# Extraer el archivo GeoTIFF de temperatura
unzip wc2.1_30s_bio.zip wc2.1_30s_bio_1.tif

# Descargar capa de provincias de Costa Rica y fundirla en un único polígono
ogr2ogr \
    -makevalid \
    -t_srs EPSG:4326 \
    -dialect sqlite \
    -sql "SELECT ST_Union(SHAPE) AS geometry FROM \"IGN_5_CO:limiteprovincial_5k\"" \
    -nln costarica \
    "costarica.gpkg" \
    WFS:"https://geos.snitcr.go.cr/be/IGN_5_CO/wfs" "IGN_5_CO:limiteprovincial_5k"

# Recortar el raster de temperatura con el contorno de Costa Rica
gdalwarp \
    -t_srs EPSG:4326 \
    -cutline "costarica.gpkg" \
    -crop_to_cutline \
    "wc2.1_30s_bio_1.tif" \
    "temperatura.tif"

# Borrar archivos temporales
rm wc2.1_30s_bio.zip
rm wc2.1_30s_bio_1.tif
rm costarica.gpkg*

```

### Precipitación

```bash
# Descargar archivo ZIP con datos de variables bioclimáticas
wget \
    "https://geodata.ucdavis.edu/climate/worldclim/2_1/base/wc2.1_30s_bio.zip" \
    -O "wc2.1_30s_bio.zip"

# Extraer el archivo GeoTIFF de temperatura
unzip wc2.1_30s_bio.zip wc2.1_30s_bio_12.tif

# Descargar capa de provincias de Costa Rica y fundirla en un único polígono
ogr2ogr \
    -makevalid \
    -t_srs EPSG:4326 \
    -dialect sqlite \
    -sql "SELECT ST_Union(SHAPE) AS geometry FROM \"IGN_5_CO:limiteprovincial_5k\"" \
    -nln costarica \
    "costarica.gpkg" \
    WFS:"https://geos.snitcr.go.cr/be/IGN_5_CO/wfs" "IGN_5_CO:limiteprovincial_5k"

# Recortar el raster de precipitación con el contorno de Costa Rica
gdalwarp \
    -t_srs EPSG:4326 \
    -cutline "costarica.gpkg" \
    -crop_to_cutline \
    "wc2.1_30s_bio_12.tif" \
    "precipitacion.tif"

# Borrar archivos temporales
rm wc2.1_30s_bio.zip
rm wc2.1_30s_bio_12.tif
rm costarica.gpkg*

```
