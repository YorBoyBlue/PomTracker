from sqlalchemy import Table, Column, Integer, VARCHAR
from database.database_manager import dbm

flag_types_table = Table('flag_types', dbm.metadata,
                         Column('id', Integer, primary_key=True),
                         Column('flag_type', VARCHAR(20), nullable=False)
                         )
