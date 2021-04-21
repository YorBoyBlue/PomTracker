from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DatabaseManager:
    SQLALCHEMY_DATABASE_URL: str
    engine: create_engine
    SessionLocal: sessionmaker
    Base: declarative_base

    def __init__(self):
        self.SQLALCHEMY_DATABASE_URL = "sqlite:///pom_tracker/database/pom_tracker.db"
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()
        self.session = self.SessionLocal()

    def get_db(self):
        return self.session


dbm = DatabaseManager()
