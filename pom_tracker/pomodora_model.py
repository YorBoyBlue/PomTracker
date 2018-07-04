import sqlite3
import datetime


class PomodoraModel:

    # Tables created for the Pom Tracker
    # c.execute("CREATE TABLE pomodoras ( "
    #           "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    #           "task BLOB,"
    #           "review BLOB,"
    #           "pom_date DATE,"
    #           "start_time TIME,"
    #           "end_time TIME"
    #           ")"
    #           )

    # c.execute("CREATE TABLE flags ( "
    #           "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    #           "flag_type VARCHAR(20)"
    #           ")"
    #           )
    #
    # c.execute("CREATE TABLE pomodoras_flags ( "
    #           "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    #           "pomodora_id INTEGER,"
    #           "flag_type VARCHAR(20)"
    #           ")"
    #           )
    # conn.commit()

    @staticmethod
    def db_connect():
        return sqlite3.connect('pomodora.db')

    @staticmethod
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

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
        conn.row_factory = self.dict_factory
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
        c = conn.cursor()

        with conn:
            c.execute("SELECT flag_type FROM flags")
            return c.fetchall()
