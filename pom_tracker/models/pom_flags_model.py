from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey
from ..database.database_manager import dbm

flags_table = Table('pomodoro_flags', dbm.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('flag_type', String, nullable=False),
                    Column('pom_id', Integer, ForeignKey('pomodoro.id'))
                    )
