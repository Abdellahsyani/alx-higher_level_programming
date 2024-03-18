#!/usr/bin/python3
"""Start link class to table in database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State)\
        .filter(State.name.collate('utf8mb4_bin') == argv[4])\
        .first()

    if query:
        print(query.id)
    else:
        print("Not found")
