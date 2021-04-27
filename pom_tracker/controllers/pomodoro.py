from datetime import datetime
import pytz

from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import select, func
from marshmallow import ValidationError
from database.database_manager import dbm

from models.flag_types_model import flag_types_table
from models.pomodoro_model import pomodoro_table
from models.pom_flags_model import flags_table
from models.pomodoro_schema import PomodoroSchema


def get_flag_types():
    with dbm() as conn:
        query = select(flag_types_table.c.flag_type)
        results = conn.execute(query).fetchall()
    return results


def get_pom_flags(pom_ids):
    with dbm() as conn:
        query = select(flags_table).where(flags_table.c.pom_id.in_(pom_ids))
        flags = conn.execute(query).fetchall()
    return flags


def get_today(user_id):
    today = datetime.now().date()
    with dbm() as conn:
        query = select(pomodoro_table).where(pomodoro_table.c.user_id == user_id,
                                             pomodoro_table.c.created == today)
        result = conn.execute(query).fetchall()

    # Get pom ids
    pom_ids = [row.id for row in result]

    # Stitch flags
    flags = get_pom_flags(pom_ids)
    poms = parse_poms(result, flags)

    return poms


def get_collection(user_id, limit, offset, date_filter, distractions_filter, unsuccessful_filter):
    with dbm() as conn:

        query = select(pomodoro_table).where(pomodoro_table.c.user_id == user_id)
        count_query = select(func.count()).where(pomodoro_table.c.user_id == user_id)

        # Apply filters
        if date_filter:
            query = query.where(pomodoro_table.c.created == date_filter)
            count_query = query.where(pomodoro_table.c.created == date_filter)
        if distractions_filter:
            query = query.where(pomodoro_table.c.distractions > 0)
            count_query = query.where(pomodoro_table.c.distractions > 0)
        if unsuccessful_filter:
            query = query.where(pomodoro_table.c.pom_success == 0)
            count_query = query.where(pomodoro_table.c.pom_success == 0)

        # Get total count
        count = conn.execute(count_query)
        total_count = count.scalar()

        # Apply limit and offset for results
        if limit:
            query = query.limit(limit)
        if offset:
            query = query.offset(offset)

        result = conn.execute(query)

        pom_rows = result.fetchall()

        # Get pom ids
        pom_ids = [row.id for row in pom_rows]

        flags = get_pom_flags(pom_ids)

    # Parse poms for collection
    poms = parse_poms(pom_rows, flags)

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
    flags_to_insert = []

    with dbm() as conn:

        try:
            # Submit pomodoros
            for time_block in time_blocks:

                times = time_block.split('-')

                start_time = datetime.strptime(times[0].strip(), '%I:%M%p').replace(
                    tzinfo=pytz.UTC)
                end_time = datetime.strptime(times[1].strip(), '%I:%M%p').replace(tzinfo=pytz.UTC)

                pom_to_insert = {
                    'user_id': user_id,
                    'distractions': distractions,
                    'pom_success': pom_success,
                    'task': task,
                    'review': review,
                    'created': today,
                    'start_time': start_time.time(),
                    'end_time': end_time.time()
                }

                insert_record = conn.execute(pomodoro_table.insert(), pom_to_insert)

                for flag in flags:
                    flags_to_insert.append({

                    })

                conn.execute(flags_table.insert(), [])
        except IntegrityError as e:
            return False

    return True


def delete(ids):
    with dbm() as conn:
        conn.execute(pomodoro_table.delete().where(pomodoro_table.c.name.in_(ids)))

        # db.query(PomodoroModel).filter(PomodoroModel.id.in_(ids)).delete(
        #     synchronize_session=False)
        # db.query(PomFlagsModel).filter(PomFlagsModel.pom_id.in_(ids)).delete(
        #     synchronize_session=False)
        # db.commit()


def export_collection(user_id, start_date, end_date):
    # Query poms within start and end dates
    with dbm() as db:
        poms = db.query(
            PomodoroModel).filter(PomodoroModel.created <= end_date).filter(
            PomodoroModel.created >= start_date).filter_by(user_id=user_id).order_by(
            PomodoroModel.created, PomodoroModel.start_time).all()

    poms = parse_poms(poms)
    return {'poms': poms}


def export_today(user_id):
    todays_poms = get_today(user_id)

    poms = parse_poms(todays_poms)
    return {'poms': poms}


def parse_poms(poms, flags):
    data = []
    for row in poms:
        pom = {
            'id': row.id,
            'user_id': row.user_id,
            'task': row.task,
            'review': row.review,
            'created': datetime.strftime(row.created, '%Y-%m-%d'),
            'distractions': row.distractions,
            'pom_success': row.pom_success,
            'start_time': row.start_time.strftime('%I:%M%p'),
            'end_time': row.end_time.strftime('%I:%M%p'),
            'flags': []
        }
        for flag in flags:
            if flag.pom_id == row.id:
                pom['flags'].append(flag.flag_type)
        data.append(pom)
    return data
