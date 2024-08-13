#!/usr/bin/python3
"""Module lists first state in `hbtn_0e_6_usa`.`states` table."""

from sqlalchemy.util.langhelpers import warn


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    )

    session = sessionmaker(bind=engine)()

    new_state = State(name="Louisiana")

    session.add(new_state)

    session.commit()
    session.close()
