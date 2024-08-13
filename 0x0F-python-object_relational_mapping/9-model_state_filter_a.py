#!/usr/bin/python3
"""List all state records"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    from model_state import Base, State

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    for instance in session.query(State).filter(State.name.like("%a%")):
        print(f"{instance.id}: {instance.name}")
