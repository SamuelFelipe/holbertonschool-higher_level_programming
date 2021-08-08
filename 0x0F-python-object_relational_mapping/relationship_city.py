#!/usr/bin/python3

'''
lists all states from the database hbtn_0e_0_usa
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    '''Model to work with sqlalchemy'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
