from sqlalchemy import Column, Integer, String, ForeignKey
from .declarative_base import Base
from sqlalchemy.orm import relationship

class Guideline(Base):
    __tablename__ = 'Guideline'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    objective_id = Column(Integer, ForeignKey('Objective.id'))
    sirap_id = Column(Integer, ForeignKey('Sirap.id'))

    # Relación con la tabla Objective
    objective = relationship("Objective", back_populates="guidelines")
    # Relación con la tabla Sirap
    sirap = relationship("Sirap", back_populates="guidelines")
    # Relación con la tabla Action
    actions = relationship("Action", back_populates="guideline")
