#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    safe = ''

    for i in sys.argv[4]:
        if i in {'\'', '\\'}:
            safe += '\\' + i
        else:
            safe += i

    match = session.query(State.id).filter(State.name == safe).first()

    if match:
        print(*match)
    else:
        print('Not found')
