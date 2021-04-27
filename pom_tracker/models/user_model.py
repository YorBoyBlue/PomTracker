from sqlalchemy import Table, Column, Integer, Text, DateTime
from database.database_manager import dbm

user_table = Table('user', dbm.metadata,
                   Column('id', Integer, primary_key=True),
                   Column('email', Text, nullable=False, unique=True),
                   Column('first_name', Text, nullable=False),
                   Column('middle_name', Text, nullable=True),
                   Column('last_name', Text, nullable=False),
                   Column('display_name', Text, nullable=True),
                   Column('password', Text, nullable=False),
                   Column('created', DateTime, nullable=False),
                   Column('modified', DateTime, nullable=False)
                   )
