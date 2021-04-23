from sqlalchemy.exc import IntegrityError
from error_handling.my_exceptions import NoSessionRecordExists
from database.database_manager import dbm
from datetime import datetime

from models.user_model import UserModel
from models.session_model import SessionModel

db = dbm()


def get_user(email):
    return db.query(UserModel).filter_by(email=email).one()


def create_user(email, first_name, middle_name, last_name, display_name, password):
    # Add user to the DB
    today = datetime.utcnow()

    user_to_add = UserModel(
        email=email,
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        display_name=display_name,
        password=password,
        created=today,
        modified=today
    )
    try:
        db.add(user_to_add)
        db.commit()
    except IntegrityError as e:
        db.rollback()
        return False
    else:
        return True


def login_user(user_id, pomodoro_login_hash):
    now = datetime.utcnow()

    # Check if user has an existing session in DB and modify it
    try:
        records_updated_count = db.query(SessionModel).filter_by(
            user_id=user_id).update({"hash": pomodoro_login_hash, "modified": now})

        if records_updated_count == 0:
            raise NoSessionRecordExists('No session for this user was found')

        db.commit()

    # Create a new session in DB if one does not exist
    except NoSessionRecordExists as e:
        session_to_add = SessionModel(user_id=user_id, hash=pomodoro_login_hash, created=now,
                                      modified=now)
        db.add(session_to_add)
        db.commit()


def logout_user(user_id):
    db.query(SessionModel).filter_by(user_id=user_id).delete(synchronize_session=False)
    db.commit()
