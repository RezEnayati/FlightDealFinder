import datetime

class FlightData:
    def __init__(self, city:str, iata_code:str, price:int):
        self.city = city
        self.iata_code = iata_code
        self.price = price
        self.date_from = ((datetime.datetime.now().date()) + datetime.timedelta(1)).strftime("%d/%m/%Y")
        self.date_to = ((datetime.datetime.now().date()) + datetime.timedelta(180)).strftime("%d/%m/%Y")

