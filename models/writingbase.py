from app import db

from .base import BaseModel, BaseSchema


class WritingBaseModel(BaseModel):

    title = db.Column(db.String(120))
    text = db.Column(db.Text)


# class BaseWritingSchema(BaseSchema):
#
#     class Meta:
#         model = WritingBaseModel
