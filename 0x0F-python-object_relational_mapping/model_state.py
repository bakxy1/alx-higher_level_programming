#!/usr/bin/python3
"""Module uses SQLAlchemy"""
from sys import argv

from sqlalchemy.orm import declarative_base
from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """states table"""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)

    pass
