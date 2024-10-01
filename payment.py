class Payment:
    id: int
    status: str
    total: int

    def __init__(self, id: int, status: str, total: int) -> None:
        self.id: id
        self.status = status
        self.total = total
