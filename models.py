from database import Base
from sqlalchemy import Column, Integer, Float, String

#creamos el modelo a partir el cual se creará la bd 
class Movie(Base):
    __tablename__ = "movie"

    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String)
    year = Column(Integer)
    stars = Column(Float)
