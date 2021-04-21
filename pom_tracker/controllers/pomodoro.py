from database.database_manager import dbm
from models.flag_types_model import FlagTypeModel
from models.pomodoro_model import PomodoroModel
from datetime import datetime

db = dbm.get_db()


def get_flag_types():
    return db.query(FlagTypeModel.flag_type).all()


def get_todays_poms(user_id):
    today = datetime.now().date()
    return db.query(PomodoroModel).filter_by(created=today, user_id=user_id).all()
