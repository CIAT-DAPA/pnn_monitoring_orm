from sqlalchemy import Column, Integer, String, ForeignKey
from .declarative_base import Base
from sqlalchemy.orm import relationship

class Milestone(Base):
	__tablename__ = 'Milestone'
	
	id = Column(Integer, primary_key=True)
	name = Column(String)
	producto_indicator = Column(String)
	obs = Column(String, nullable=True)
	action_id = Column(Integer, ForeignKey('Action.id'))

	# Relación con la tabla Action
	action = relationship("Action", back_populates="milestones")
	# Relación con la tabla Detail
	details = relationship("Detail", back_populates="milestone")

