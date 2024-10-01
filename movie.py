class Movie:
    id: int
    name: str
    duration: int  # in mins

    def __init__(self, id: int , name: str, duration: int):
        self.id = id
        self.name = name
        self.duration = duration
