from flask import Blueprint, jsonify, request, g
from models.edit import Edit, EditSchema
from models.writing import Writing
from lib.secure_route import secure_route_editor


api = Blueprint('edits', __name__)
edit_schema = EditSchema()

@api.route('/edits', methods=['GET'])
def index():
    edits = Edit.query.all()
    return edit_schema.jsonify(edits, many=True), 200


@api.route('/edits', methods=['POST'])
@secure_route_editor
def create():
    data = request.get_json()
    print(data)
    edit, errors = edit_schema.load(data)
    print(edit, errors)
    if errors:
        return jsonify(errors), 422

    edit.editor = g.current_editor
    edit.save()
    return edit_schema.jsonify(edit), 201

@api.route('/edits/<int:edit_id>', methods=['GET'])
def showEdit(edit_id):
    edit = Edit.query.get(edit_id)
    if not edit:
        return jsonify({'message': 'not found'}), 404
    return edit_schema.jsonify(edit), 200



@api.route('/writings/<int:writing_id>/edits', methods=['GET'])
def showEdits(writing_id):
    edits = Edit.query.join(Edit.original).filter(Writing.id == writing_id).all()
    print(edits)
    if not edits:
        return jsonify({'message': 'not found'}), 404
    return edit_schema.jsonify(edits, many=True), 200

# @api.route('/writings/<int:writing_id>/edits/<int:edit_id>', methods=['GET'])
# def showSingleEdit(writing_id, edit_id):
#     edit = Edit.query.join(Edit.original).filter(Writing.id == writing_id).all()
#
#     if not edit:
#         return jsonify({'message': 'not found'}), 404
#     return edit_schema.jsonify(edit), 200


@api.route('/edits/<int:edit_id>/like', methods=['POST'])
@secure_route_editor
def like(edit_id):

    data = request.get_json()
    print(data['rating'])
    edit = Edit.query.get(edit_id)
    print(edit)
    if not edit:
        return jsonify({'message': 'Not Found'}), 404
    edit.liked_by.append(g.current_editor)
    edit.rating = data['rating']
    edit.save()
    return edit_schema.jsonify(edit), 201
