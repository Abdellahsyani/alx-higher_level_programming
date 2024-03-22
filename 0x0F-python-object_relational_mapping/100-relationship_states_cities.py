#!/usr/bin/python3
"""

Create schema of 1TM database
1 To Many relationship using mysqlalchemy

"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City, Base
from relationship_state import State

if __name__ == "__main__":
    db_str = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(db_str)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco")

    new_state.cities.append(new_city)
    result = session.query(State).all()

    session.add(new_state)
    session.commit()
