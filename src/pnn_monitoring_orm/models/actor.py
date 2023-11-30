from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Actor(Base):
    __tablename__= 'Actor'

    id = Column(Integer, primary_key=True)
    institution_id = Column(Integer, ForeignKey("Institution.id"))
    detail_id = Column(Integer, ForeignKey("Detail.id"))

    # Relación con la tabla Actor
    institution = relationship("Institution", back_populates="actors")
    # Relación con la tabla Detail
    detail = relationship("Detail", back_populates="actors")