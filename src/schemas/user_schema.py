from marshmallow import Schema, fields, validate

class UserSchema(Schema):
  username = fields.String(required=True, validate=validate.Length(min=3, max=80))
  email = fields.Email(required=True)
  password = fields.String(required=True, validate=validate.Length(min=6))