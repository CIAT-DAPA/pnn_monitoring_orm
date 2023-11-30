from sqlalchemy import Column, Integer, String, ForeignKey
from .declarative_base import Base
from sqlalchemy.orm import relationship

class Action(Base):    
	__tablename__ = 'Action'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	guideline_id = Column(Integer, ForeignKey('Guideline.id'))

	# Relación con la tabla Guideline
	guideline = relationship("Guideline", back_populates="actions")
	# Relación con la tabla Milestone
	milestones = relationship("Milestone", back_populates="action")