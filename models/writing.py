from app import db, ma
from marshmallow import fields
# pylint: disable=W0611
from .writer import Writer
# from .edit import EditSchema
from .category import Category

from .base import BaseSchema
from .writingbase import WritingBaseModel


writing_categories = db.Table(
    'writing_categories',
    db.Column('writing_id', db.Integer, db.ForeignKey('writings.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))
)



class Writing(db.Model, WritingBaseModel):

    __tablename__ = 'writings'

    notes = db.Column(db.Text, nullable=True)
    author = db.relationship('Writer', backref='created_writings')
    author_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    categories = db.relationship('Category', secondary=writing_categories, backref='writings')
    active = db.Column(db.Boolean, default=True)




class WritingSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Writing

    author = fields.Nested('WriterSchema', only=('id', 'username'))
