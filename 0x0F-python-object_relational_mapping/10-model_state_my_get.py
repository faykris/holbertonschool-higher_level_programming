#!/usr/bin/python3
"""
10. Get a state
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    i = 0
    for state in session.query(State).filter(State.name == argv[4]):
        i += 1
    if i != 0:
        print("{}".format(i))
    else:
        print("Not found")
    session.close()
