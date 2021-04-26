from sqlalchemy import Table, Column, Integer, VARCHAR
from database.database_manager import dbm

flag_types_table = Table('flag_types', dbm.metadata,
                         Column('id', Integer, primary_key=True),
                         Column('flag_type', VARCHAR(20), nullable=False)
                         )

# class FlagTypeModel(dbm.Base):
#     __tablename__ = 'flag_types'
#
#     id = Column(Integer, primary_key=True)
#     flag_type = Column(VARCHAR(20), nullable=False)
#
#     def __repr__(self):
#         return "<FlagTypeModel(flag_type='%s')>" % self.flag_type
