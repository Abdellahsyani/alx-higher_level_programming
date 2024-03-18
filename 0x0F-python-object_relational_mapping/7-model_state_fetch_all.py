#!/usr/bin/python3
"""usage: start using the SQLAlchemy """

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"\
            .format(argv[1], argv[2], argv[3]))
    Base.metadata.craete_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)
    for row in query.all():
        print("{}: {}".format(row.id, row.name))

