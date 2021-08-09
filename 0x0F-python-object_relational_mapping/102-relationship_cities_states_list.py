#!/usr/bin/python3
"""
14. Cities in state
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    new_state = State(name='California')
    session.add(new_state)
    session.commit()

    new_city = City(name='San Francisco')
    session.add(new_city)
    session.commit()

    session.close()
