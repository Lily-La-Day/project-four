from app import db, ma
from marshmallow import fields
from .writer import Writer
from .base import BaseSchema
from .writingbase import WritingBaseModel





class Writing(db.Model, WritingBaseModel):

    __tablename__ = 'writings'

    notes = db.Column(db.Text, nullable=True)
    author = db.relationship('Writer', backref='created_writings')
    author_id = db.Column(db.Integer, db.ForeignKey('writers.id'))



class WritingSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Writing

    author = fields.Nested('WriterSchema', only=('id', 'username'))
