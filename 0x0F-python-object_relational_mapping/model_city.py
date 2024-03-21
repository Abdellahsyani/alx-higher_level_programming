#!/usr/bin/python3

"""

City class

"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class City(Base):
    """The City class will abstract the implementation of City table"""
    __tablename__ = "cities"

    id = Column(Integer,
            autoincrement=True,
            primary_key=True,
            unique=True,
            nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    def __repr__(self):
        return f"{self.id}: {self.name}"
