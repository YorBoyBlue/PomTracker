from sqlalchemy import Column, Integer, VARCHAR
from models.base_model import BaseModel


class FlagTypeModel(BaseModel):
    __tablename__ = 'flag_types'

    id = Column(Integer, primary_key=True)
    flag_type = Column(VARCHAR(20), nullable=False)

    def __repr__(self):
        return "<FlagTypeModel(flag_type='%s')>" % self.flag_type

    @staticmethod
    def get_flag_types():
        pass
        # Session = sessionmaker(bind=engine)
        # session = Session()
        # flags = session.query(FlagTypeModel.flag_type).all()
        # return flags
