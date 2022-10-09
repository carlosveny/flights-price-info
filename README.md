# flights-price-info
Programa en Python que obtiene el precio más barato de un vuelo dados una serie de parámetros, y usando la API de Flightlabs. Después, guarda los datos del vuelo obtenido en un fichero CSV. 

La finalidad de este programa es ejecutarlo cada día para ver como cambian los precios de un vuelo según el día en que se realiza la compra.

## Instalación
Todo el programa funciona sobre Python 3.8.7 por lo que es necesario que esté instalado en el sistema. Además, también es recomendable tener instalado Pip para la instalación de módulos.
1. Registrarse en Flightlabs para obtener una API_KEY (https://www.goflightlabs.com/).
2. Clonar el repo.
3. Renombrar el archivo 'api-key_example.config' a 'api-key.config'.
4. Añadir la API_KEY de Flightlabs en el archivo 'api-key.config'. (LA API KEY VA SIN COMILLAS).
5. Instalar el módulo 'requests', si no se tiene ya instalado, con el comando `pip install requests `
6. Ejecutar el programa `python main.py`

### Parámetros
Los parámetros se pueden modificar según se necesiten

| Parámetro       | Valor inicial | Descripción                                               |
|-----------------|:--------------|-----------------------------------------------------------|
| ORIGIN          | 'PMI'         | Aeropuerto de origen del vuelo, según su código IATA |
| DESTINATION     | 'MAD'         | Aeropuerto de destino del vuelo, según su código IATA |
| DEPARTURE_DATE  | '2022-11-02'  | Fecha de salida del vuelo, en formato 'YYYY-MM-DD' |
| ADULTS          | 1             | Número de pasajeros adultos |
| CURRENCY        | 'EUR'         | Moneda, según la ISO 4217 |
| MOCKED          | False         | Si es *True* la petición no se realiza a la API si no que se mockea con el archivo correspondiente. Sirve para hacer pruebas sin gastar las peticiones de la API |
