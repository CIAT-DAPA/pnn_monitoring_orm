from sqlalchemy import Column, Integer, String, ForeignKey
from .declarative_base import Base
from sqlalchemy.orm import relationship

class Action_type(Base):    
	__tablename__ = 'Action_type'

	id = Column(Integer, primary_key=True)
	name = Column(String(50))

	# Relación con la tabla Action
	actions = relationship("Action", back_populates="action_type")