from model.models import Base
from model.attribute import Attribute
from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import relationship

class AttributeDetail(Base):
    __tablename__ = 'attribute_detail'
    __table_args__ = {'schema': 'cat'}
    nbr = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)

    available = Column(Boolean, nullable=False, default=True)

    attribute_nbr = Column(ForeignKey('cat.attribute.nbr'),
                            nullable=False,
                            index=True)

    attribute = relationship(Attribute)
