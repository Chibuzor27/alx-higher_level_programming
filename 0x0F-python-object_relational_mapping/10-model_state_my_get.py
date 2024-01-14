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

    item = session.query(State).filter(
            State.name == sys.argv[4]).order_by(State.id).first()
    if item:
        print(item.id)
    else:
        print("Not found")

    session.close()
