from functools import wraps
import jwt
from flask import request, jsonify, g
from models.writer import Writer
from models.editor import Editor
from config.environment import secret

def secure_route(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return jsonify({'message': 'Unauthorized'}), 401
        token = request.headers.get('Authorization').replace('Bearer ', '')

        try:
            payload = jwt.decode(token, secret)
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token Expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid Token'}), 401

        writer = Writer.query.get(payload.get('sub'))

        if not writer:
            return jsonify({'message': 'Unauthorized'}), 401

        g.current_writer = writer

        return func(*args, **kwargs)
    return wrapper


def secure_route_editor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return jsonify({'message': 'Unauthorized'}), 401
        token = request.headers.get('Authorization').replace('Bearer ', '')

        try:
            payload = jwt.decode(token, secret)
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token Expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid Token'}), 401

        editor = Editor.query.get(payload.get('sub'))

        if not editor:
            return jsonify({'message': 'Unauthorized'}), 401

        g.current_editor = editor

        return func(*args, **kwargs)
    return wrapper
