from sqlalchemy import Column, Integer, String, ForeignKey, Double, Date
from .declarative_base import Base
from sqlalchemy.orm import relationship

class Detail(Base):
    __tablename__ = 'Detail'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    amount = Column(Double)
    quantity = Column(Integer)
    date = Column(Date)
    goal = Column(Integer)
    period_id = Column(Integer, ForeignKey("Period.id"))
    product_id = Column(Integer, ForeignKey("Product.id"))
    implemented_value = Column(Double)
    base_line = Column(Integer)
    milestone_id = Column(Integer, ForeignKey("Milestone.id"))

    # Relación con la tabla Period
    period = relationship("Period", back_populates="details")
    # Relación con la tabla Annuity
    times = relationship("Time", back_populates="detail")
    # Relación con la tabla Product
    product = relationship("Product", back_populates="details")
    # Relación con la tabla Milestone
    milestone = relationship("Milestone", back_populates="details")

    # Relación con la tabla Actor
    actors = relationship("Actor", back_populates="detail")
    # Relación con la tabla Responsible
    responsibles = relationship("Responsible", back_populates="detail")


