#!/usr/bin/python3
"""
8. First state
"""
from model_state import Base, State, engine, Session

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).first()
    if state is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
