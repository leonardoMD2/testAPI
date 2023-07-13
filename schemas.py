from pydantic import BaseModel
from typing import Optional

class MovieModel(BaseModel):
    title:str
    year:int
    stars:float