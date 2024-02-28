from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_data = data_manager.get_flight_data()

flight_search = FlightSearch()
flight_search.search_for_flight(flight_data=flight_data,flyFrom= "LAX")