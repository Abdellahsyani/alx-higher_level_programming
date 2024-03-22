#!/usr/bin/python3

"""FETCH all
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    db_str = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
        format(argv[1], argv[2], argv[3])
    engine = create_engine(db_str)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).\
        join(City, City.state_id == State.id).\
        order_by(City.id).all()

    for state, city in result:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.commit()
