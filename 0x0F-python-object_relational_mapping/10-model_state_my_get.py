#!/usr/bin/python3

'''
prints the <<State>> object with the <<name>> passed as argument
from the database <<hbtn_0e_6_usa>>
'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    '''
take 4 arguments: <<mysql username>>, <<mysql password>>,
<<database name>> and <<state name to search>>
'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    string = ''

    for i in sys.argv[4]:
        if i in {'\'', '\\'}:
            string += '\\' + i
        else:
            string += i

    result = session.query(State.id).filter(State.name == string).first()

    if result:
        print(*result)
    else:
        print('Not found')
