#!/usr/bin/python3
"""Here is the definition of a class to be mapped as a SQL table"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, String)


Base = declarative_base()


class State(Base):
    """The definition of the states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(128))
