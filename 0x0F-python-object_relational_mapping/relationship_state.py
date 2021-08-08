#!/usr/bin/python3

'''
lists all <<states>> from the database <<hbtn_0e_0_usa>>
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    '''State class with sqlalchemy'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete')
