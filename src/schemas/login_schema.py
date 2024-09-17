from marshmallow import Schema, fields, validate

class LoginSchema(Schema):
  username = fields.String(required=True, validate=validate.Length(min=3, max=80))
  password = fields.String(required=True, validate=validate.Length(min=6))