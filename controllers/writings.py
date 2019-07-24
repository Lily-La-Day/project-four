from flask import Blueprint
from models.writing import Writing, WritingSchema

api = Blueprint('writings', __name__)
writing_schema = WritingSchema()


@api.route('/writings', methods=['GET'])
def index():
    writings = Writing.query.all()
    return writing_schema.jsonify(writings, many=True), 200
