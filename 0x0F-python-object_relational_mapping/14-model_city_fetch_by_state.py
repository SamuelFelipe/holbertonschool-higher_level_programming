#!/usr/bin/python3

'''
prints all City objects from the database hbtn_0e_14_usa
'''


import sys
from model_city import Base, City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    '''
take 3 arguments: <<mysql username>>, <<mysql password>> and <<database name>>
'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    match = session.query(State.name, City.id, City.name).join(State)

    for i in match:
        print('{}: ({}) {}'.format(i[0], i[1], i[2]))
