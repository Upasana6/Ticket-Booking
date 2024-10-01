from payment import Payment
from seat import Seat
from shows import Show


class Booking:
    show: Show
    seats: list[Seat]
    payment: Payment
