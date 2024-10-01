from enum import Enum


class Category(Enum):
    RECLINER = "recliner"
    GOLD = "silver"
    SILVER = "silver"


class Seat:
    id: int
    row: str
    category: Category
    price: int
