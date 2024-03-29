#!/usr/bin/python3
""" Fetch States """


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    records = session.query(State).filter(
            State.name.contains('a')).order_by(State.id)
    for item in records:
        print('{}: {}'.format(item.id, item.name))

    session.close()
