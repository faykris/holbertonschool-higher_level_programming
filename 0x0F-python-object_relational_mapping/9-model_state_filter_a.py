#!/usr/bin/python3
"""
9. Contains `a`
"""
from model_state import Base, State, engine, Session

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state in session.query(State).filter(State.name.like("%a%"))\
            .order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
