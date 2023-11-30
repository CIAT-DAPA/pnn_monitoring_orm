from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Year(Base):
    __tablename__ = 'Year'

    id = Column(Integer, primary_key=True)
    value = Column(Integer)

    # Relación con la tabla Time
    times = relationship("Time", back_populates="year")
