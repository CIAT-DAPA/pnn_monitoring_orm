from sqlalchemy import Column, Integer, String
from .declarative_base import Base
from sqlalchemy.orm import relationship

class Product(Base):
	__tablename__ = 'Product'
	id =  Column(Integer, primary_key=True)
	name = Column(String(255))
	ext_id = Column(String(50))
	
	# Relación con la tabla Detail
	details = relationship("Detail", back_populates="product")
