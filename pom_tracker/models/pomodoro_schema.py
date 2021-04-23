from marshmallow import Schema, fields, validates, ValidationError


class PomodoroSchema(Schema):
    task = fields.Str(required=True,
                      error_messages={
                          'null': 'You must provide a Title for the task(s) you were working on.'
                      })
    review = fields.Str(required=True,
                        error_messages={
                            'null': 'You must provide a Description of the task(s) you were '
                                    'working on.'
                        })
    flags = fields.List(fields.Str(), required=True,
                        error_messages={
                            'null': 'You must choose one or more Flags related to the task(s) you '
                                    'were working on.'
                        })
    time_blocks = fields.List(fields.Str(), required=True,
                              error_messages={
                                  'null': 'You must choose one or more Time Blocks related to the '
                                          'task(s) you were working on.'
                              })

    # @validates('task')
    # def validate_task(self, value):
    #     if not value:
    #         raise ValidationError("You must provide a Title for the task you were working on.")
    #
    # @validates('review')
    # def validate_review(self, value):
    #     if not value:
    #         raise ValidationError(
    #             "You must provide a Description for the task you were working on.")
