from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Time(Base):
    __tablename__ = 'Time'

    id = Column(Integer, primary_key=True)
    detail_id = Column(Integer, ForeignKey('Detail.id'))
    year_id = Column(Integer, ForeignKey('Year.id'))

    # Relación con la tabla Detail
    detail = relationship("Detail", back_populates="times")

    # Relación con la tabla Year
    year = relationship("Year", back_populates="times")
