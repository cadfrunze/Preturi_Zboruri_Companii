import requests
from datetime import datetime
from data_base import APP_KEY_TEQ
API_TEQ_SEARCH = 'https://api.tequila.kiwi.com/v2/search'
MY_CITY: str = 'Cluj-Napoca'
MY_IATA: str = 'CLJ'
# print(APP_KEY_TEQ)
header_teq: dict = {
    'apikey': str(APP_KEY_TEQ)

}


paramtri_search = {
    'fly_from': MY_IATA,
    'fly_to': 'NUE',
    'date_from': f'{datetime.now().strftime("%d/%m/%Y")}',
    'date_to': f'{datetime.now().strftime(f"29/%m/%Y")}'
}

cerere_test = requests.get(url=API_TEQ_SEARCH, headers=header_teq, params=paramtri_search)
print(cerere_test.text)



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass