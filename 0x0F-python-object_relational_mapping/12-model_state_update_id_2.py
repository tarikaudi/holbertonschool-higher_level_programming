#!/usr/bin/python3
"""comment aaa"""

import sqlalchemy
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = sqlalchemy.create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
        )
    Base.metadata.create_all(engine)
    session = sqlalchemy.orm.Session(engine)
    session.query(State).filter(State.id == 2).update({'name': 'New Mexico'})
    session.commit()
    session.close()
