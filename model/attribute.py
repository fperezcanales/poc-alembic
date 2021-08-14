from model.models import Base
from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import relationship

class Attribute(Base):
    __tablename__ = 'attribute'
    __table_args__ = {'schema': 'cat'}
    nbr = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)

    available = Column(Boolean, nullable=False, default=True)