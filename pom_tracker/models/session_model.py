from sqlalchemy import Column, Integer, Text, DateTime
from models.base_model import BaseModel


class SessionModel(BaseModel):
    __tablename__ = 'session'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, unique=True)
    hash = Column(Text, nullable=False, unique=True)
    create_date = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Session(id='%s', hash='%s', create_date='%s')>" % (
            self.id, self.hash, self.create_date)
