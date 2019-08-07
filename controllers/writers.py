from flask import Blueprint, jsonify, request, g
from models.writer import Writer, WriterSchema
from models.writing import Writing
from lib.secure_route import secure_route
# from models.edit import Edit, EditSchema


api = Blueprint('edits', __name__)
api = Blueprint('writers', __name__)
writer_schema = WriterSchema()

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    writer, errors = writer_schema.load(data)
    if errors:
        return jsonify(errors), 422
    writer.save()
    return jsonify({'message': 'Registration Successful'}), 201

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Unauthorized'}), 401
    writer = Writer.query.filter_by(email=data['email']).first()
    if not writer or not writer.validate_password(data['password']):
        return jsonify({'message': 'Unauthorized'}), 401
    return jsonify({
        'token': writer.generate_token(),
        'message': f'Welcome back {writer.username}'
    }), 200

@api.route('/writers', methods=['GET'])
def index():
    writers = Writer.query.all()
    return writer_schema.jsonify(writers, many=True), 200

@api.route('/writerprofile', methods=['GET'])
@secure_route
def profile():
    return writer_schema.jsonify(g.current_writer), 200
