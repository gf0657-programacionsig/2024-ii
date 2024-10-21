# Datos agrupados por GBIF

## Registros de presencia de *Puma concolor* en Costa Rica

El archivo CSV comprimido como ZIP debe descargarse de:  
[https://www.gbif.org/occurrence/download/0025023-241007104925546](https://www.gbif.org/occurrence/download/0025023-241007104925546).

```shell
# Generación de archivo CSV con menos columnas de datos
ogr2ogr \
  gbif-puma-concolor-cri.csv \
  /vsizip/0025023-241007104925546.zip/0025023-241007104925546.csv \
  -sql "SELECT species, eventDate, locality, decimalLongitude, decimalLatitude \
        FROM \"0025023-241007104925546\""
```
