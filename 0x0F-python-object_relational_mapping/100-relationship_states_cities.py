#!/usr/bin/python3

'''
script that adds the State object “Louisiana”
to the database <<hbtn_0e_6_usa>>
'''


import sys
from relationship_state import Base, State
from relationship_city import City
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

    new_state = State(name='California')

    new_city = City(name='San Francisco', state_id=new_state.id)

    session.add(new_state)
    session.add(new_city)

    session.commit()
