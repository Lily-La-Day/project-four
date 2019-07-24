from marshmallow import fields
from app import db, ma
from .userbase import BaseUserModel, BaseUserSchema

class Editor(db.Model, BaseUserModel):

    __tablename__ = 'editors'


class EditorSchema(ma.ModelSchema, BaseUserSchema):

    created_edits = fields.Nested('EditSchema', many=True)

    class Meta:
        model = Editor
