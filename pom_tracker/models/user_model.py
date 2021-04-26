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

# class UserModel(dbm.Base):
#     __tablename__ = 'user'
#
#     id = Column(Integer, primary_key=True)
#     email = Column(Text, nullable=False, unique=True)
#     first_name = Column(Text, nullable=False)
#     middle_name = Column(Text, nullable=True)
#     last_name = Column(Text, nullable=False)
#     display_name = Column(Text, nullable=True)
#     password = Column(Text, nullable=False)
#     created = Column(DateTime, nullable=False)
#     modified = Column(DateTime, nullable=False)
#
#     def __repr__(self):
#         return "<User(id='%s', email='%s', first_name=%s, middle_name='%s', " \
#                "last_name='%s', display_name='%s', password='%s', " \
#                "created='%s', modified='%s')>" % (
#                    self.id, self.email, self.first_name, self.middle_name,
#                    self.last_name, self.display_name, self.password,
#                    self.created, self.modified)
