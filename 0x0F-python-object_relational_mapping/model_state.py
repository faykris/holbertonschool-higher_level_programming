#!/usr/bin/python3
"""
6. First state model
"""
from sys import argv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

port = 3306
connection = """mysql+mysqldb://{}:{}@localhost:{}/{}
             """.format(argv[1], argv[2], port, argv[3])
engine = create_engine(connection)
Base = declarative_base()


class State(Base):
    """State - Class"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


session = Session(engine)
session.close()
