#!/usr/bin/python3
"""
7. All states via SQLAlchemy
"""
from model_state import Base, State, engine, Session

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
