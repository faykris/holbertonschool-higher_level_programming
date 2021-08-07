#!/usr/bin/python3
"""
10. Get a state
"""
import sys
from model_state import Base, State, engine, Session

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = Session(engine)
    i = 0
    for state in session.query(State).filter(State.name == sys.argv[4]):
        i += 1
    if i != 0:
        print("{}".format(i))
    else:
        print("Not found")
    session.close()
