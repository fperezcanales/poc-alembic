from model.models import Base
from model.category import Category
from model.attribute import Attribute
from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import relationship

class CategoryAttribute(Base):
    __tablename__ = 'category_attribute'
    __table_args__ = {'schema': 'cat'}

    category_nbr = Column(ForeignKey('cat.category.nbr'), primary_key=True,
                           nullable=False,
                           index=True)

    attribute_nbr = Column(ForeignKey('cat.attribute.nbr'), primary_key=True,
                            nullable=False,
                            index=True)

    category = relationship(Category)
    attribute = relationship(Attribute)
