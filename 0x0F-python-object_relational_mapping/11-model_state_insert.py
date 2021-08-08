#!/usr/bin/python3

'''
script that adds the State object “Louisiana”
to the database <<hbtn_0e_6_usa>>
'''


import sys
from model_state import Base, State
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

    new_state = State(name='Louisiana')

    session.add(new_state)

    session.commit()
    print(new_state.id)
