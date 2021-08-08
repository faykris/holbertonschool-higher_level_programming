#!/usr/bin/python3
"""
10. Get a state
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for row in session.query(State.name, City.id, City.name)\
            .join(City, State.id == City.state_id).order_by(City.id).all():
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
    session.close()
