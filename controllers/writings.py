from flask import Blueprint, jsonify, request, g
from models.writing import Writing, WritingSchema
from models.category import Category
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
    print(g.current_writer)
    writing.save()
    return writing_schema.jsonify(writing), 201

@api.route('/writings/<int:writing_id>', methods=['GET'])
def show(writing_id):
    writing = Writing.query.get(writing_id)
    if not writing:
        return jsonify({'message': 'not found'}), 404
    return writing_schema.jsonify(writing), 200


@api.route('/writings/<int:writing_id>', methods=['POST'])
def deactivate(writing_id):
    writing = Writing.query.get(writing_id)


    # data = request.get_json()
    # print(data['rating'])
    # edit = Edit.query.get(edit_id)
    # print(edit)
    # if not edit:
    #     return jsonify({'message': 'Not Found'}), 404
    writing.active=False
    # edit.rating = data['rating']
    writing.save()
    return writing_schema.jsonify(writing), 201
