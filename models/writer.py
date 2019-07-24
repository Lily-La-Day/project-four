from marshmallow import fields
from app import db, ma
from .userbase import BaseUserModel, BaseUserSchema

class Writer(db.Model, BaseUserModel):

    __tablename__ = 'writers'


class WriterSchema(ma.ModelSchema, BaseUserSchema):

    created_writings = fields.Nested('WritingSchema', many=True)

    class Meta:
        model = Writer
