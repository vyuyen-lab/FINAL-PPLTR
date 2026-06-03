from abc import ABC, abstractmethod

class Ticket(ABC):
    def __init__(self, ticket_id, flight_id, passenger_id, base_price):
        self._ticket_id = ticket_id
        self._flight_id = flight_id
        self._passenger_id = passenger_id
        self._base_price = base_price

    @property
    def base_price(self):
        return self._base_price

    @base_price.setter
    def base_price(self, value):
        if value < 0:
            raise ValueError("Giá vé không được âm!") 
        self._base_price = value

    @abstractmethod
    def calculate_total_price(self):
        pass
class EconomyTicket(Ticket):
    def __init__(self, ticket_id, flight_id, passenger_id, base_price, extra_luggage_kg=0):
        super().__init__(ticket_id, flight_id, passenger_id, base_price)
        self.extra_luggage_kg = extra_luggage_kg

    def calculate_total_price(self):
        return self._base_price + (self.extra_luggage_kg * 50000)

class BusinessTicket(Ticket):
    def __init__(self, ticket_id, flight_id, passenger_id, base_price, special_meal=True):
        super().__init__(ticket_id, flight_id, passenger_id, base_price)
        self.special_meal = special_meal

    def calculate_total_price(self):
        return self._base_price + 500000