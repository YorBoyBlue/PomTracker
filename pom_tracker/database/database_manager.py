from sqlalchemy import create_engine, MetaData


# from sqlalchemy.ext.declarative import declarative_base


# from sqlalchemy.orm import sessionmaker


class DatabaseManager:
    SQLALCHEMY_DATABASE_URL: str
    engine: create_engine
    metadata: MetaData

    # SessionLocal: sessionmaker
    # Base: declarative_base

    def __init__(self):
        self.SQLALCHEMY_DATABASE_URL = "sqlite:///pom_tracker/database/pom_tracker.db"
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URL)
        # self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.metadata = MetaData()
        # self.Base = declarative_base()

    # def get_db(self):
    #     return self.SessionLocal()
    #     # db = self.SessionLocal()
    #     # try:
    #     #     yield db
    #     # finally:
    #     #     db.close()

    def __call__(self):
        return self.engine.connect()
        # return self.SessionLocal()


dbm = DatabaseManager()
