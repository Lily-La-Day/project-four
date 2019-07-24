from flask import Blueprint
from models.writing import Writing, finalschema

api = Blueprint('finals', __name__)
writing_schema = finalschema()


@api.route('/finals', methods=['GET'])
def index():
    finals = Writing.query.all()
    return writing_schema.jsonify(finals, many=True), 200
