from marshmallow import Schema, fields


class PomodoraSchema(Schema):
    task = fields.Str(required=True)
    review = fields.Str(required=True)
    flags = fields.List(fields.Str(), required=True)
