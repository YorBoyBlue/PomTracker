import sqlite3
import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///pom_tracker.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# class PomodoraModel(Base):
#     __tablename__ = 'pomodora'
#
#     id = Column(Integer, primary_key=True)
#     task = Column(String, nullable=False)
#     review = Column(String, nullable=False)
#     pom_date = Column(Date, nullable=False)
#     start_time = Column(Time, nullable=False)
#     end_time = Column(Time, nullable=False)
#
#     def __repr__(self):
#         return "<Pomodora(task='%s', review='%s', pom_date='%s', " \
#                "start_time='%s', end_time='%s')>" % (
#                    self.task, self.review, self.pom_date, self.start_time,
#                    self.end_time)
#
#
# Base.metadata.create_all(engine)

# Tables created for the Pom Tracker
# conn = sqlite3.connect('pomodora.db')
# c = conn.cursor()
# c.execute("CREATE TABLE pomodoras ( "
#           "id INTEGER PRIMARY KEY AUTOINCREMENT,"
#           "task BLOB,"
#           "review BLOB,"
#           "pom_date DATE,"
#           "start_time TIME,"
#           "end_time TIME, "
#           "UNIQUE(pom_date, start_time) ON CONFLICT REPLACE"
#           ")"
#           )
#
# # c.execute("CREATE TABLE flags ( "
# #           "id INTEGER PRIMARY KEY AUTOINCREMENT,"
# #           "flag_type VARCHAR(20)"
# #           ")"
# #           )
#
# c.execute("CREATE TABLE pomodoras_flags ( "
#           "id INTEGER PRIMARY KEY AUTOINCREMENT,"
#           "pomodora_id INTEGER,"
#           "flag_type VARCHAR(20)"
#           ")"
#           )
# conn.commit()


class PomodoraModel:

    @staticmethod
    def db_connect():
        return sqlite3.connect('databases/pomodora.db')

    def insert_pom_and_pom_flags(self, pom):
        self.insert_pom(pom)
        self.insert_pom_flags(pom)

    def insert_pom(self, pom):
        conn = self.db_connect()
        c = conn.cursor()
        times = pom.time_block.split('-')
        start_time = times[0]
        end_time = times[1]
        today = datetime.date.today()
        with conn:
            c.execute(
                "INSERT INTO pomodoras(task, review, start_time, end_time, "
                "pom_date) "
                "VALUES (:task, :review, :start_time, :end_time, :pom_date)",
                {'task': pom.current_task, 'review': pom.review,
                 'start_time': start_time, 'end_time': end_time,
                 'pom_date': today})

    def insert_pom_flags(self, pom):
        conn = self.db_connect()
        c = conn.cursor()
        today = datetime.date.today()
        times = pom.time_block.split('-')
        start_time = times[0]

        with conn:
            c.execute(
                "SELECT id FROM pomodoras WHERE pom_date=:today AND "
                "start_time=:start_time",
                {'today': today, 'start_time': start_time})
            pom_ids = c.fetchall()
            for pom_id in pom_ids:
                for flag in pom.flags:
                    c.execute(
                        "INSERT INTO pomodoras_flags(pomodora_id, flag_type) "
                        "VALUES (:pomodora_id,:flag_type)",
                        {'pomodora_id': pom_id[0], 'flag_type': flag})

    def get_flag_types(self):
        conn = self.db_connect()
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        with conn:
            c.execute("SELECT flag_type FROM flags")
            return c.fetchall()

    def get_todays_poms(self):
        conn = self.db_connect()
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        today = datetime.date.today()

        with conn:
            c.execute(
                "SELECT *"
                "FROM pomodoras "
                "WHERE pom_date=:today "
                "ORDER BY start_time",
                {'today': today})
            return c.fetchall()

    def get_flags_by_pom_id(self, pom_id):
        conn = self.db_connect()
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        with conn:
            c.execute("SELECT flag_type FROM pomodoras_flags "
                      "WHERE pomodora_id=:pom_id",
                      {'pom_id': pom_id})
            return c.fetchall()
