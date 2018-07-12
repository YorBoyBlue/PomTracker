from sqlalchemy import Column, Integer, Text, Time, Date, UniqueConstraint
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class PomodoraModel(BaseModel):
    __tablename__ = 'pomodora'

    id = Column(Integer, primary_key=True)
    task = Column(Text, nullable=False)
    review = Column(Text, nullable=False)
    add_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    flags = relationship('PomFlagsModel', back_populates="pom")

    __table_args__ = (UniqueConstraint('add_date', 'start_time',
                                       name='date_start_time_uc',
                                       ),
                      )

    def __repr__(self):
        return "<Pomodora(id='%s', task='%s', review='%s', flags=%s, " \
               "add_date='%s', start_time='%s', end_time='%s')>" % (
                   self.id, self.task, self.review, self.flags, self.add_date,
                   self.start_time, self.end_time)
