from app import db, ma
from marshmallow import fields
from .writingbase import WritingBaseModel
from .base import BaseSchema




class Final(db.Model, WritingBaseModel):

    __tablename__ = 'finals'

    edit_id = db.Column(db.Integer, db.ForeignKey('edits.id'))
    edit = db.relationship('Edit', backref='created_edits')




class FinalSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Final

    edit = fields.Nested('EditSchema', only=('id', ))
