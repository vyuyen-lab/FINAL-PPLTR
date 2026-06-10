from abc import ABC, abstractmethod
from models.flight import Flight  # Nhập lớp Flight để thiết lập mối liên kết giữa 2 file

class Ticket(ABC):
    def __init__(self, ticket_id, passenger_id, flight: Flight, auto_book=True):
        self._ticket_id = ticket_id
        self._passenger_id = passenger_id
        self._flight = flight  

        if auto_book:
            self._flight.book_seat()

    @property
    def ticket_id(self):
        return self._ticket_id

    @property
    def passenger_id(self):
        return self._passenger_id

    @property
    def flight(self):
        return self._flight

    @property
    def base_price(self):
        return self._flight.base_price
    
    @abstractmethod
    def calculate_total_price(self):
        pass


class EconomyTicket(Ticket):
    def __init__(self, ticket_id, passenger_id, flight: Flight, extra_luggage_kg=0, auto_book=True):

        super().__init__(ticket_id, passenger_id, flight, auto_book)
        self.extra_luggage_kg = extra_luggage_kg

    def calculate_total_price(self):

        return self.base_price + (self.extra_luggage_kg * 50000)


class BusinessTicket(Ticket):
    def __init__(self, ticket_id, passenger_id, flight: Flight, special_meal=True, auto_book=True):
        super().__init__(ticket_id, passenger_id, flight, auto_book)
        self.special_meal = special_meal

    def calculate_total_price(self):
        meal_fee = 500000 if self.special_meal else 0
        return self.base_price + meal_fee