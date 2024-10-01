from theatre import Theatre


class TheatreController:
    theatre_map: dict[str, list[Theatre]]
    all_theatres: list[Theatre]

    def __init__(self, theatre_map: dict[str, list[Theatre]], all_theatres: list[Theatre]) -> None:
        self.theatre_map = theatre_map
        self.all_theatres = all_theatres
