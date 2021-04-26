from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship
from database.database_manager import dbm

flags_table = Table('pomodoro_flags', dbm.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('flag_type', String, nullable=False),
                    Column('pom_id', Integer, ForeignKey('pomodoro.id'))
                    )

# class PomFlagsModel(dbm.Base):
#     __tablename__ = 'pomodoro_flags'
#
#     id = Column(Integer, primary_key=True)
#     flag_type = Column(String, nullable=False)
#     pom_id = Column(Integer, ForeignKey('pomodoro.id'))
#
#     pom = relationship('PomodoroModel', back_populates="flags")
#
#     def __repr__(self):
#         return "<Flags(flag_type='%s')>" % self.flag_type
