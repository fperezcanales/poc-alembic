from model.models import Base
from model.category import Category
from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'cat'}
    nbr = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)

    isOnline = Column(Boolean, nullable=False, default=False)
    available = Column(Boolean, nullable=False, default=True)
    price = Column(Integer, nullable=False, default=0)

    category_nbr = Column(ForeignKey('cat.category.nbr'),
                            nullable=False,
                            index=True)

    category = relationship(Category)

    