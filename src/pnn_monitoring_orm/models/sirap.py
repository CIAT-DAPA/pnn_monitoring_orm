from sqlalchemy import Column, Integer, String, ForeignKey
from .declarative_base import Base
from sqlalchemy.orm import relationship

class Sirap(Base):
    __tablename__ = 'Sirap'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String)
    region = Column(String(50))
    prot_areas = Column(String)
    ext_id = Column(String(50), nullable=True)

    # Relación con la tabla Guideline
    guidelines = relationship("Guideline", back_populates="sirap")

