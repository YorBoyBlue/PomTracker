from datetime import datetime
import pytz

from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from database.database_manager import dbm

from models.flag_types_model import FlagTypeModel
from models.pomodoro_model import PomodoroModel
from models.pom_flags_model import PomFlagsModel
from models.pomodoro_schema import PomodoroSchema

db = dbm.get_db()


def get_flag_types():
    return db.query(FlagTypeModel.flag_type).all()


def get_today(user_id):
    today = datetime.now().date()
    return db.query(PomodoroModel).filter_by(created=today, user_id=user_id).all()


def get_collection(user_id, limit, offset, date_filter, distractions_filter, unsuccessful_filter):
    query = db.query(PomodoroModel).filter_by(user_id=user_id)

    # Apply filters
    if date_filter:
        query = query.filter_by(created=date_filter)
    if distractions_filter:
        query = query.filter(PomodoroModel.distractions > 0)
    if unsuccessful_filter:
        query = query.filter_by(pom_success=0)

    # Get total count
    total_count = query.count()

    # Apply limit and offset
    if limit:
        query = query.limit(limit)
    if offset:
        query = query.offset(offset)

    pom_rows = query.all()

    # Parse flags
    poms = []
    for row in pom_rows:
        flags = []
        for flag in row.flags:
            flags.append(flag.flag_type)
        pom = {
            'task': row.task,
            'review': row.review,
            'created': row.created.strftime('%Y-%m-%d'),
            'distractions': row.distractions,
            'flags': flags,
            'pom_success': row.pom_success,
            'start_time': row.start_time.strftime('%I:%M%p').strip('0'),
            'end_time': row.end_time.strftime('%I:%M%p').strip('0')
        }
        poms.append(pom)

    return {
        'poms': poms,
        'total_count': total_count
    }


def validate(task, review, flags, time_blocks):
    try:
        PomodoroSchema().load(
            {'task': task, 'review': review, 'flags': flags, 'time_blocks': time_blocks})
    except ValidationError as err:
        # User is missing 1 or more required fields
        message = ''
        for k, v in err.messages.items():
            message += '<br> * ' + v[0]
        return {
            'validated': False,
            'message': message
        }

    else:
        return {
            'validated': True,
            'message': 'Success!'
        }


def insert_poms(user_id, task, review, flags, distractions, pom_success, time_blocks):
    today = datetime.now().date()

    # Submit pomodoros
    for time_block in time_blocks:

        times = time_block.split('-')

        start_time = datetime.strptime(times[0].strip(), '%I:%M%p').replace(tzinfo=pytz.UTC)
        end_time = datetime.strptime(times[1].strip(), '%I:%M%p').replace(tzinfo=pytz.UTC)

        # Create pomodoro model object to submit to DB
        pom_to_add = PomodoroModel(
            user_id=user_id,
            distractions=distractions,
            pom_success=pom_success,
            task=task,
            review=review,
            created=today,
            start_time=start_time.time(),
            end_time=end_time.time()
        )
        for flag in flags:
            pom_to_add.flags.append(PomFlagsModel(flag_type=flag))

        # Add pom to the DB
        db.add(pom_to_add)

    try:
        db.commit()
    except IntegrityError as e:
        # Pomodoro already exists with that time block
        db.rollback()
        return False

    return True


def delete(ids):
    db.query(PomodoroModel).filter(PomodoroModel.id.in_(ids)).delete(
        synchronize_session=False)
    db.query(PomFlagsModel).filter(PomFlagsModel.pom_id.in_(ids)).delete(
        synchronize_session=False)
    db.commit()


def export_collection(user_id, start_date, end_date):
    # Query poms within start and end dates
    poms = db.query(
        PomodoroModel).filter(PomodoroModel.created <= end_date). \
        filter(PomodoroModel.created >= start_date).filter_by(
        user_id=user_id).order_by(
        PomodoroModel.created, PomodoroModel.start_time).all()

    data = {'poms': []}
    for row in poms:
        pom = {
            'created': datetime.strftime(row.created, '%Y-%m-%d'),
            'title': row.task,
            'start_time': row.start_time.strftime('%I:%M%p'),
            'end_time': row.end_time.strftime('%I:%M%p'),
            'distractions': row.distractions,
            'pom_success': row.pom_success,
            'review': row.review,
            'flags': []
        }
        for flag in row.flags:
            pom['flags'].append(flag.flag_type)
        data['poms'].append(pom)
    return data


def export_today(user_id):
    todays_poms = get_today(user_id)

    data = {'poms': []}
    for row in todays_poms:
        pom = {
            'created': datetime.strftime(row.created, '%Y-%m-%d'),
            'title': row.task,
            'start_time': row.start_time.strftime('%I:%M%p'),
            'end_time': row.end_time.strftime('%I:%M%p'),
            'distractions': row.distractions,
            'pom_success': row.pom_success,
            'review': row.review,
            'flags': []
        }
        for flag in row.flags:
            pom['flags'].append(flag.flag_type)
        data['poms'].append(pom)
    return data
