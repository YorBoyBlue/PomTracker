from sqlalchemy import Column, Integer, Text, String, Date, Time, \
    UniqueConstraint
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class PomodoraModel(BaseModel):
    __tablename__ = 'pomodora'

    id = Column(Integer, primary_key=True)
    task = Column(Text, nullable=False)
    review = Column(Text, nullable=False)
    date = Column(Date, nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)

    # flags = relationship('PomFlagsModel', back_populates="pom")

    # __table_args__ = (UniqueConstraint('pom_date', 'start_time',
    #                                    name='date_start_time_uc'),)

    def __repr__(self):
        return "<Pomodora(task='%s', review='%s', pom_date='%s', " \
               "start_time='%s', end_time='%s')>" % (
                   self.task, self.review, self.date, self.start_time,
                   self.end_time)
