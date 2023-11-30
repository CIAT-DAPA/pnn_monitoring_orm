from sqlalchemy import Column, Integer, String
from .declarative_base import Base
from sqlalchemy.orm import relationship

class Objective(Base):
	__tablename__ = 'Objective'

	id = Column(Integer, primary_key=True)
	name = Column(String(255))
	description = Column(String)
	ext_id= Column(String(50), nullable=True)

	# Relación con la tabla Guideline
	guidelines = relationship("Guideline", back_populates="objective")
