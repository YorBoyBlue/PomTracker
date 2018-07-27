from marshmallow import Schema, fields


class PomodoraSchema(Schema):
    task = fields.Str(required=True,
                      error_messages={
                          'null': 'You must provide a Title for the task you '
                                  'were working on.'
                      })
    review = fields.Str(required=True,
                        error_messages={
                            'null': 'You must provide a Description of the '
                                    'task you were working on.'
                        })
    flags = fields.List(fields.Str(), required=True,
                        error_messages={
                            'null': 'You must choose one or more Flags '
                                    'related to the task you were working on.'
                        })
