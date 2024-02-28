import requests
from flight_search import FlightSearch
from flight_data import FlightData

SHEETY_ENDPOINT = "Sheety Api"

# TASK 1: read the data from the Google sheet and give us a list of the cities in the sheet
class DataManager:
    def __init__(self):
        self.response = requests.get(url=SHEETY_ENDPOINT)
        self.response.raise_for_status()
        self.sheet_data = self.response.json()
        self.post_iata_code()
        self.get_flight_data()

    def post_iata_code(self):
        flight_search = FlightSearch()
        for i in range(len(self.sheet_data["prices"])):
            endpoint = SHEETY_ENDPOINT + "/" + str(i + 2)
            iata_code = {
                "price": {
                    "iataCode": flight_search.get_iata_code(self.sheet_data["prices"][i]["city"])
                }
            }
            response = requests.put(url=endpoint, json=iata_code)
            response.raise_for_status()

    def get_flight_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        data_list = response.json()['prices']
        flight_data_list = []
        for data in data_list:
            flight_data_list.append(FlightData(city=data['city'], iata_code=data["iataCode"],price=data["lowestPrice"]))
        return flight_data_list


