#!/usr/bin/python3
"""
6. First state model
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

connection = "mysql://" + sys.argv[1] + ":" + sys.argv[2] +\
             "@localhost:3306/" + sys.argv[3]
engine = create_engine(connection)
Base = declarative_base()


class State(Base):
    """State - Class"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
session = Session(engine)
session.close()
