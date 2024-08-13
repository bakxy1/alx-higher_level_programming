#!/usr/bin/python3
"""Module lists first state in `hbtn_0e_6_usa`.`states` table."""

from sqlalchemy.util.langhelpers import warn


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])
    )

    session = sessionmaker(bind=engine)()

    first_record = session.query(State).first()

    if first_record:
        print("{}: {}".format(first_record.id, first_record.name))
    else:
        print("Nothing")
