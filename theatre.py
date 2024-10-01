from screen import Screen
from shows import Show


class Theatre:
    id: int
    address: str
    city: str
    screens: list[Screen]
    shows: list[Show]

    def __init__(self, id: int, address: str, city: str, screens: list[Screen], shows: list[Show]) -> None:
        self.id = id
        self.address = address
        self.city = city
        self.screens = screens
        self.shows = shows
    