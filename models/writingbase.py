from app import db

from .base import BaseModel, BaseSchema


class WritingBaseModel(BaseModel):

    title = db.Column(db.String(120), nullable=False)
    text = db.Column(db.Text, nullable=False)


# class BaseWritingSchema(BaseSchema):
#
#     class Meta:
#         model = WritingBaseModel
