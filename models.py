from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# class RootCause(Base):  
#     __tablename__ = 'root_cause'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)

class Bug(Base):
    __tablename__ = 'bug'
    __table_args__ = {'schema': 'poc'}

    nbr = Column(Integer, primary_key=True)
    description = Column(String)

    # def __repr__(self):
    #     return 'id: {}, root cause: {}'.format(self.id, self.root_cause)