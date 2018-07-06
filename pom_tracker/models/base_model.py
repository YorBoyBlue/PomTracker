from uuid import uuid4
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class BaseModel:
    def __init__(self, *args, **kwargs):
        # Helps with inspections and linters
        super().__init__(*args, **kwargs)

    @staticmethod
    def gen_uuid():
        return str(uuid4())
