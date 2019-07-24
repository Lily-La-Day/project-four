from app import db

from .base import BaseModel


class WritingBaseModel(BaseModel):

    title = db.Column(db.String(120))
    text = db.Column(db.Text)
