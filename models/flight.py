class Flight:
    def __init__(self, flight_id, destination, base_price, available_seats):
        self._flight_id = flight_id
        self._destination = destination
        self._base_price = base_price
        self._available_seats = available_seats

    @property
    def flight_id(self): return self._flight_id

    @property
    def destination(self): return self._destination

    @property
    def base_price(self): return self._base_price

    @property
    def available_seats(self): return self._available_seats

    @available_seats.setter
    def available_seats(self, value):
        if value < 0:
            raise ValueError("Số ghế không thể âm!")
        self._available_seats = value

    def to_dict(self):
        return {
            "flight_id": self._flight_id, 
            "destination": self._destination, 
            "base_price": self._base_price, 
            "available_seats": self._available_seats
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["flight_id"], data["destination"], data["base_price"], data["available_seats"])