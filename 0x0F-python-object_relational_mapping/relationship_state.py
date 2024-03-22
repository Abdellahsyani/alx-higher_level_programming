#!/usr/bin/python3

"""

State class

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base

class State(Base):
    """The State class will abstract the implementation of states table"""
    __tablename__ = "states"

    id = Column(Integer,
            autoincrement=True,
            primary_key=True,
            unique=True,
            nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    def __repr__(self):
        return f"{self.id}: {self.name}"
