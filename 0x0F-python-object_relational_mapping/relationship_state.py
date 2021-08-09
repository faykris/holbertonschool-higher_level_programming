#!/usr/bin/python3
"""
6. First state model
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import City


Base = declarative_base()


class State(Base):
    """State - Class"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True,
                unique=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state = relationship(City, backref='cities')


class City2(City):
    pass
