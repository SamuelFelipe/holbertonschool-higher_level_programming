#!/usr/bin/python3

'''
prints the first <<State>> object from the database <<hbtn_0e_6_usa>>
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

    result = session.query(State.id, State.name).filter(State.id == 1).first()

    if result:
        print('{}: {}'.format(result[0], result[1]))
    else:
        print()
