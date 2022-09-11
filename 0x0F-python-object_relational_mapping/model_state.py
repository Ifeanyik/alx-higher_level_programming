#!/usr/bin/python3
'''This module defines a State class'''
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("mysql+mysqldb://root:@localhost:3306/mysql")

class State(Base):
    '''State class implementation'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)

engine.connect()
