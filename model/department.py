from model.models import Base
from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean

class Deparment(Base):
    __tablename__ = 'department'
    __table_args__ = {'schema': 'cat'}
    nbr = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)


