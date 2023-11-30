from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Institution(Base):
    __tablename__= 'Institution'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    ext_id = Column(String(50))

    # Relación con la tabla Actor
    actors = relationship("Actor", back_populates="institution")
    # Relación con la tabla Responsible
    responsibles = relationship("Responsible", back_populates="institution")

    