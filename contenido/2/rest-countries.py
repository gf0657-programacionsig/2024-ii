import requests
import json

# Nombre del país
pais = input("Ingrese el nombre de un país: ")

# URL
url = f'https://restcountries.com/v3.1/name/{pais}'

# Solicitud GET
respuesta = requests.get(url)

# Verificación de la respuesta
if respuesta.status_code == 200:
    # La solicitud fue exitosa

    # Se cargan en formato JSON los datos retornados en una lista
    datos = respuesta.json()

    # Se cargan los datos del primer país de la lista
    datos_pais = datos[0]

    # Se seleccionan elementos de datos específicos
    nombre_comun = datos_pais['name']['common']
    capital = datos_pais.get('capital', ['No disponible'])[0]
    region = datos_pais.get('region', 'No disponible')
    poblacion = datos_pais.get('population', 'No disponible')
    monedas = datos_pais.get('currencies', {})
    idiomas = datos_pais.get('languages', {})

    # Se unen las monedas en una hilera de texto
    lista_monedas = ', '.join([moneda['name'] for moneda in monedas.values()])

    # Se unen los idiomas en una hilera de texto
    lista_idiomas = ', '.join(idiomas.values())

    print(f"\nInformación sobre {nombre_comun}:")
    print(f"Capital: {capital}")
    print(f"Región: {region}")
    print(f"Población: {poblacion} habitantes")
    print(f"Moneda(s): {lista_monedas}")
    print(f"Idioma(s): {lista_idiomas}")
else:
    # Se produjo un error
    print(f"Error {respuesta.status_code}")