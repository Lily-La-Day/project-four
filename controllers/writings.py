from flask import Blueprint, jsonify, request, g
from models.writing import Writing, WritingSchema
# from lib.helpers import is_unique
from lib.secure_route import secure_route

api = Blueprint('writings', __name__)
writing_schema = WritingSchema()


@api.route('/writings', methods=['GET'])
def index():
    writings = Writing.query.all()
    return writing_schema.jsonify(writings, many=True), 200

@api.route('/writings', methods=['POST'])
@secure_route
def create():
    data = request.get_json()
    writing, errors = writing_schema.load(data)

    if errors:
        return jsonify(errors), 422

    writing.author = g.current_writer
    writing.save()
    return writing_schema.jsonify(writing), 201