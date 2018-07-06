from OldCode.helpers.base import Base, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, VARCHAR


class FlagTypeModel(Base):
    __tablename__ = 'flag_types'

    id = Column(Integer, primary_key=True)
    flag_type = Column(VARCHAR(20), nullable=False)

    def __repr__(self):
        return "<FlagTypeModel(flag_type='%s')>" % self.flag_type

    @staticmethod
    def get_flag_types():
        Session = sessionmaker(bind=engine)
        session = Session()
        flags = session.query(FlagTypeModel.flag_type).all()
        return flags


Base.metadata.create_all(engine)
