import requests
from notification_manager import NotificationManager
TEQUILA_API_KEY = "Tquila API Key"
TEQUILA_END_POINT_IATA = "https://api.tequila.kiwi.com"


class FlightSearch:
    def __init__(self):
        self.header = {"apikey": TEQUILA_API_KEY}
        self.notif_manager = NotificationManager()

    def get_iata_code(self, city_name: str):
        endpoint = TEQUILA_END_POINT_IATA + "/locations/query"
        params = {
            "term": city_name
        }
        response = requests.get(url=endpoint, params=params, headers=self.header)
        response.raise_for_status()
        location_data = response.json()
        return location_data['locations'][0]['code']

    def search_for_flight(self, flight_data:list, flyFrom:str):
        endpoint = TEQUILA_END_POINT_IATA + "/v2/search"
        for flight in flight_data:
            params = {
                "fly_from": flyFrom,
                "fly_to": flight.iata_code,
                "date_from": flight.date_from,
                "date_to": flight.date_to,
                "price_to": flight.price,
                "sort": "price",
                "limit": 1,
                "curr": "USD",
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
            }
            response = requests.get(url=endpoint, params=params, headers=self.header)
            response.raise_for_status()
            ticket_data = response.json()
            if ticket_data['_results'] != 0:
                date_from = ticket_data['data'][0]['route'][0]['local_departure'].split("T")[0]
                date_to = ticket_data['data'][0]['route'][1]['local_departure'].split("T")[0]
                body = (f"Low Price Alert! Only ${ticket_data['data'][0]['price']} to fly from {ticket_data['data'][0]['cityFrom']} "
                        f"to {ticket_data['data'][0]['cityTo']}."
                        f"From: {date_from} "
                        f"to: {date_to}.")
                self.notif_manager.send_sms(body)
            else:
                body = "No tickets found! :("   
                self.notif_manager.send_sms(body)

