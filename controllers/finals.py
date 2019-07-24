from flask import Blueprint, jsonify, request, g
from models.final import Final, FinalSchema
from lib.secure_route import secure_route_editor

api = Blueprint('finals', __name__)
final_schema = FinalSchema()


@api.route('/finals', methods=['GET'])
def index():
    finals = Final.query.all()
    return final_schema.jsonify(finals, many=True), 200

@api.route('/finals', methods=['POST'])
@secure_route_editor
def create():

    data = request.get_json()
    final, errors = final_schema.load(data)

    if errors:
        return jsonify(errors), 422

    final.editor = g.current_editor
    final.save()
    return final_schema.jsonify(final), 201
