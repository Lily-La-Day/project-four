from flask import Blueprint, jsonify, request, g
from models.final import Final, FinalSchema
from models.edit import Edit, EditSchema
from lib.secure_route import secure_route_editor, secure_route

api = Blueprint('finals', __name__)
final_schema = FinalSchema()


@api.route('/finals', methods=['GET'])
def index():
    finals = Final.query.all()
    return final_schema.jsonify(finals, many=True), 200

@api.route('/finals', methods=['POST'])
@secure_route
def create():

    data = request.get_json()
    print(data)
    final, errors = final_schema.load(data)

    if errors:
        return jsonify(errors), 422

    final.writer = g.current_writer
    final.save()
    return final_schema.jsonify(final), 201


# @api.route('/final/<int:edit_id>', methods=['GET'])
#
# def showFinal(edit_id):
#     final = Final.query.join(Final.edit).filter(Edit.id == edit_id).all()
#     print(final)
#     # final, errors = final_schema.load(final)
#     if not final:
#         return jsonify({'message': 'not found'}), 404
#     return final_schema.jsonify(final, many=True), 201

@api.route('/final/<int:final_id>', methods=['GET'])
def showFinal(final_id):
    final = Final.query.get(final_id)
    if not final:
        return jsonify({'message': 'not found'}), 404
    return final_schema.jsonify(final), 200
