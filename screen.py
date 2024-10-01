from seat import Seat


class Screen:
    id: int
    seats: list[Seat]

    def __init__(self, id: int, seats: list[Seat]) -> None:
        self.id = id
        self.seats = seats
