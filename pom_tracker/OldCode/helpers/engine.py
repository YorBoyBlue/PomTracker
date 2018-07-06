from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///databases/pom_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()
