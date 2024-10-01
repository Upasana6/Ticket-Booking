import datetime
from screen import Screen
from movie import Movie
from seat import Seat


class Show:
    id: int
    movie: Movie
    screen: Screen
    start_time: datetime
    booked_seats: list[Seat]

    def __init__(self, id:int, movie:Movie, screen: Screen, start_time: datetime, booked_seats: list[Seat]=[]) -> None:
        self.id = id
        self.movie = movie
        self.screen = screen
        self.start_time = start_time
        self.booked_seats = booked_seats
    
    def book_seat(self, seat: Seat) -> str:
        if seat not in self.booked_seats:
            self.booked_seats.append(seat)
            return "Seat booked successfully"
        return "Selected seat is already booked"
