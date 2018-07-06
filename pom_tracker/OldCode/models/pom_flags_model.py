from OldCode.helpers.base import Base, engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class PomFlagsModel(Base):
    __tablename__ = 'pomodora_flags'

    id = Column(Integer, primary_key=True)
    flag_type = Column(String, nullable=False)
    pom_id = Column(Integer, ForeignKey('pomodora.id'))

    pom = relationship('PomodoraModel', back_populates="flags")

    def __repr__(self):
        return "<Flags(flag_type='%s')>" % self.flag_type


Base.metadata.create_all(engine)
