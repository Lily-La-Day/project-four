from flask import Blueprint, jsonify, request
from models.editor import Editor, EditorSchema


api = Blueprint('editors', __name__)
editor_schema = EditorSchema()


@api.route('/editorregister', methods=['POST'])
def register():
    data = request.get_json()
    editor, errors = editor_schema.load(data)
    if errors:
        return jsonify(errors), 422
    editor.save()
    return jsonify({'message': 'Registration Successful'}), 201

@api.route('/editorlogin', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Unauthorized'}), 401
    editor = Editor.query.filter_by(email=data['email']).first()
    if not editor or not editor.validate_password(data['password']):
        return jsonify({'message': 'Unauthorized'}), 401
    return jsonify({
        'token': editor.generate_token(),
        'message': f'Welcome back {editor.username}'
    }), 200



@api.route('/editors', methods=['GET'])
def index():
    editors = Editor.query.all()
    return editor_schema.jsonify(editors, many=True), 200
