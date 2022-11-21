from pydantic import BaseModel
from TypeItem import TypeItem


class Item(BaseModel):
    id: int
    nameItem: str
    type: TypeItem
    director: str
    number_of_votes: int
    average_grade: float
    sum_grade:float
    url: str = ""
