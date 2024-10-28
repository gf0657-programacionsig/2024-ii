# Datos del Instituto Geográfico Nacional (IGN)

## División territorial administrativa

WFS: https://geos.snitcr.go.cr/be/IGN_5_CO/wfs

Lista de capas

```bash
# Lista de capas en el servicio WFS
ogrinfo -ro WFS:"https://geos.snitcr.go.cr/be/IGN_5_CO/wfs" -summary
```

```
INFO: Open of `WFS:https://geos.snitcr.go.cr/be/IGN_5_CO/wfs'
      using driver `WFS' successful.
Metadata:
  TITLE=SNIT Web Feature Service
  ABSTRACT=This is the reference implementation of WFS 1.0.0 and WFS 1.1.0, supports all WFS operations including Transaction.
  PROVIDER_NAME=The Ancient Geographers
1: IGN_5_CO:curvas_5000_2017 (title: Curvas de nivel cada 10 metros 1:5.000 año 2017 (Costa Rica) (Capa escalada))
2: IGN_5_CO:limitedistrital_5k (title: DTA (Límite Distrital))
3: IGN_5_CO:limitecantonal_5k (title: Límite Cantonal)
4: IGN_5_CO:limiteprovincial_5k (title: Límite Provincial)
```

### Provincias

```bash
# Descargar capa de provincias
ogr2ogr \
    -makevalid \
    -t_srs EPSG:4326 \
    -nln provincias \
    "provincias.gpkg" \
    WFS:"https://geos.snitcr.go.cr/be/IGN_5_CO/wfs" "IGN_5_CO:limiteprovincial_5k"

```

### Cantones

```bash
# Descargar capa de cantones
ogr2ogr \
    -makevalid \
    -t_srs EPSG:4326 \
    -nln cantones \
    "cantones.gpkg" \
    WFS:"https://geos.snitcr.go.cr/be/IGN_5_CO/wfs" "IGN_5_CO:limitecantonal_5k"

```

### Distritos

```bash
# Descargar capa de distritos
ogr2ogr \
    -makevalid \
    -t_srs EPSG:4326 \
    -nln distritos \
    "distritos.gpkg" \
    WFS:"https://geos.snitcr.go.cr/be/IGN_5_CO/wfs" "IGN_5_CO:limitedistrital_5k"

```
