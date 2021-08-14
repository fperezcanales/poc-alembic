from model.models import Base
from model.department import Deparment
from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = 'category'
    __table_args__ = {'schema': 'cat'}
    nbr = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)

    isOnline = Column(Boolean, nullable=False, default=False)

    department_nbr = Column(ForeignKey('cat.department.nbr'),
                            nullable=False,
                            index=True)

    department = relationship(Deparment)