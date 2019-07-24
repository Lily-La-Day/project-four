from flask import Blueprint, jsonify, request, g
from models.edit import Edit, EditSchema
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
    print('editting')
    data = request.get_json()
    edit, errors = edit_schema.load(data)

    if errors:
        return jsonify(errors), 422

    edit.editor = g.current_editor
    edit.save()
    return edit_schema.jsonify(edit), 201
