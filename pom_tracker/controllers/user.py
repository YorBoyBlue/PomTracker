from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import select
from ..error_handling.my_exceptions import NoSessionRecordExists
from ..database.database_manager import dbm
from datetime import datetime

from ..models.user_model import user_table
from ..models.session_model import session_table


def get_user(email):
    with dbm() as conn:
        query = select(user_table).where(user_table.c.email == email)
        result = conn.execute(query)
        user = result.fetchone()
    return user


def create_user(email, first_name, middle_name, last_name, display_name, password):
    # Add user to the DB
    today = datetime.utcnow()

    with dbm() as conn:
        try:
            query = user_table.insert().values(
                email=email,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                display_name=display_name,
                password=password,
                created=today,
                modified=today
            )
            conn.execute(query)
        except IntegrityError as e:
            return False
        else:
            return True


def login_user(user_id, pomodoro_login_hash):
    now = datetime.utcnow()

    with dbm() as conn:
        # Check if user has an existing session in DB and modify it
        try:
            query = session_table.update().where(session_table.c.user_id == user_id).values(
                hash=pomodoro_login_hash, modified=now)
            rows_affected = conn.execute(query)

            if rows_affected.rowcount == 0:
                raise NoSessionRecordExists('No session for this user was found')

        # Create a new session in DB if one does not exist
        except NoSessionRecordExists as e:
            query = session_table.insert().values(user_id=user_id, hash=pomodoro_login_hash,
                                                  modified=now, created=now)
            conn.execute(query)


def logout_user(user_id):
    with dbm() as conn:
        query = session_table.delete().where(session_table.c.user_id == user_id)
        conn.execute(query)
