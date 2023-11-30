from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Responsible(Base):
    __tablename__= 'Responsible'

    id = Column(Integer, primary_key=True)
    institution_id = Column(Integer, ForeignKey("Institution.id"))
    detail_id = Column(Integer, ForeignKey("Detail.id"))

    # Relación con la tabla Institution
    institution = relationship("Institution", back_populates="responsibles")
    # Relación con la tabla Detail
    detail = relationship("Detail", back_populates="responsibles")