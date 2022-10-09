import configparser
import json
import requests
import csv
from datetime import datetime

# Global values
ORIGIN = 'PMI' # IATA Code
DESTINATION = 'MAD' # IATA Code
DEPARTURE_DATE = '2022-11-02' # yyyy-mm-dd format
ADULTS = 1
CURRENCY = 'EUR' # Currency code (ISO 4217)
MOCKED = False # Mocked or actual request

# Read access-key from .config file
configParser = configparser.RawConfigParser()
configFilePath = r'api-key.config'
configParser.read(configFilePath)

# Get mocked request (MOCKED = True)
response = None
if (MOCKED):
    print('Mocking request...\n')
    try:
        f = open('mocked-request.json')
    except:
        print('ERROR: file "mocked-request.json" not found')
        exit()
    response = json.load(f)

# Get request to FlightLabs API (MOCKED = False)
else:
    print('Making request to FlightLabs API...\n')
    params = {
        'access_key': configParser.get('api-key', 'access-key'),
        'origin': ORIGIN,
        'destination': DESTINATION,
        'departureDate': DEPARTURE_DATE,
        'adults': ADULTS,
        'currency': CURRENCY,
    }
    api_result = requests.get('https://app.goflightlabs.com/search-best-flights', params)
    response = api_result.json()
    if not response['success']:
        print('ERROR: Invalid API Key')
        exit()

# Format response
print('Cheapest flights:')
cheapestFlights = next((x for x in response['data']['buckets'] if x['id'] == 'Cheapest'), None)
flights = []
for idx, f in enumerate(cheapestFlights['items']):
    flightData = [
        datetime.today().strftime('%d-%m-%Y'),
        f['price']['raw'],
        f['legs'][0]['carriers']['marketing'][0]['name'],
        f['legs'][0]['departure'],
        f['legs'][0]['arrival'],
    ]
    print(str(idx+1) + '. ' + str(flightData[1]) + '€ | ' + flightData[2] + ', ' + flightData[3] + ', ' + flightData[4])
    flights.append(flightData)

# Save to csv file
    f = open('best-flights-prices.csv', 'a+', newline='')
writer = csv.writer(f)
writer.writerow(flights[0])
print('\nBest flight appended to "best-flights-prices.csv"\n')
