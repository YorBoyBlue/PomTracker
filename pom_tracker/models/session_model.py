from sqlalchemy import Table, Column, Integer, Text, DateTime
from ..database.database_manager import dbm

session_table = Table('session', dbm.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('user_id', Integer, nullable=False, unique=True),
                      Column('hash', Text, nullable=False, unique=True),
                      Column('created', DateTime, nullable=False),
                      Column('modified', DateTime, nullable=False)
                      )
