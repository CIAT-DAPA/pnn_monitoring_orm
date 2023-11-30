from sqlalchemy import Column, Integer, String
from .declarative_base import Base
from sqlalchemy.orm import relationship

class Period(Base):
	__tablename__ = 'Period'
	id =  Column(Integer, primary_key=True)
	name = Column(String(255))
	
	# Relación con la tabla Detail
	details = relationship("Detail", back_populates="period")
