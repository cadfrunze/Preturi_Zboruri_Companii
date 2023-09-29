from data_base import *
import requests
import pandas as pd
# exemplu: "prices": [
    # {
    #   "city": "Paris",
    #   "iataCode": "",
    #   "lowestPrice": 54,
    #   "id": 2
    # }
print(END_POINT_SHEETY)
header: dict = {
    'Content-Type': 'application/json',
    'Authorization': AUTHORIZATION_SHEETY
}

orase: dict = {
    'Paris': 'PAR CDG LBG ORY',
    'Berlin': 'BER SXF TXL THF',
    'Tokyo': 'TYO HND NRT',
    'Sydney': 'SYD',
    'Istanbul': 'IST SAW',
    'Bucharest': 'BUH OTP',
    'New York': 'JFK LGA EWR NYC',
    'San Francisco': 'SFO',
    'Cape Town': 'CPT',
    'Nuremberg': 'NUE'
}

# parcurgere: int = 2
# for element in orase:
#     editare_iata: dict = {
#         'price': {
#             'iataCode': orase[element]
#         }
#     }
#     cerere_put = requests.put(url=f'{END_POINT_SHEETY}{parcurgere}', headers=header, json=editare_iata)
#     parcurgere = parcurgere + 1
#     print(cerere_put.text)
coduri: str = orase['Berlin']
print(coduri.split(' '))
