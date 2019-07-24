from app import db, ma
from marshmallow import fields
from .writing import Writing
from .writer import WriterSchema, Writer
from .writingbase import WritingBaseModel
from .base import BaseSchema

likes = db.Table(
    'likes',
    db.Column('edit_id', db.Integer, db.ForeignKey('edits.id')),
    db.Column('editor_id', db.Integer, db.ForeignKey('editors.id'))
)


class Edit(db.Model, WritingBaseModel):

    __tablename__ = 'edits'

    original_id = db.Column(db.Integer, db.ForeignKey('writings.id'))
    original = db.relationship('Writing', backref='created_writings')
    editor = db.relationship('Editor', backref='created_edits')
    editor_id = db.Column(db.Integer, db.ForeignKey('editors.id'))
    liked_by = db.relationship('Editor', secondary=likes, backref='likes')



class EditSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Edit

    editor = fields.Nested('EditorSchema', only=('id', 'username'))
    liked_by = fields.Nested('EditorSchema', many=True, only=('id', 'username'))
    original = fields.Nested('WriterSchema', only=('id', 'username'))
