from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///pom_tracker.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class PomFlagsModel(Base):
    __tablename__ = 'pomodora_flags'

    id = Column(Integer, primary_key=True)
    flag_type = Column(String, nullable=False)
    pom_id = Column(Integer, ForeignKey('pomodora.id'))

    pom = relationship("Pomodora", back_populates="pomodora_flags")

    def __repr__(self):
        return "<Flags(flag_type='%s')>" % self.flag_type


Base.metadata.create_all(engine)
