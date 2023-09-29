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
print(cerere_test)

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    """Va prelua datele prin API, conform cerintelor proiectului"""
    def __init__(self) -> None:
        self.range_zi = 2
        self.ziua_calendar: int = datetime.now().day
        self.luna_calendar: int = datetime.now().month
        self.an_calendar: int = datetime.now().year
        self.lista_orase: list = []
        self.check_days()
        
    def check_days(self) -> None:
        """Verificare luna, zi calendaristica cu variabila range_zi"""
        try:
            self.zi = datetime(year=self.an_calendar, month=self.luna_calendar, day=(self.ziua_calendar + self.range_zi))
        except ValueError:
            self.range_zi = self.range_zi - 1
            if self.luna_calendar > 12:
                self.luna_calendar = 1
                self.an_calendar: int = 1
        #     self.zi = datetime(year=self.an_calendar, month=self.luna_calendar, day=self.range_zi)
        # print(self.zi)
    def cautare_zboruri(self) -> None:
        """Metoda responsabila cu cautare zboruri companii aeriene"""
        pass
cautare_zboruri: object = FlightSearch()
