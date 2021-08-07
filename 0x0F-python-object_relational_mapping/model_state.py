#!/usr/bin/python3
"""
6. First state model
"""
from sys import argv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


connection = "mysql+mysqldb://{}:{}@{}:{}/{}"\
            .format(argv[1], argv[2], "localhost", 3306, argv[3])

engine = create_engine(connection)
Base = declarative_base()


class State(Base):
    """State - Class"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
