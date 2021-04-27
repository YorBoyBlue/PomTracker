from sqlalchemy import create_engine, MetaData


class DatabaseManager:
    SQLALCHEMY_DATABASE_URL: str
    engine: create_engine
    metadata: MetaData

    def __init__(self):
        self.SQLALCHEMY_DATABASE_URL = "sqlite:///pom_tracker/database/pom_tracker.db"
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URL)
        self.metadata = MetaData()

    def __call__(self):
        return self.engine.connect()


dbm = DatabaseManager()
