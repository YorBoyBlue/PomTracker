from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///databases/pom_tracker.db')
Base = declarative_base()
