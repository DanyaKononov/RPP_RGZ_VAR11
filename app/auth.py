from functools import wraps
from flask import request, jsonify
import os

def authenticate(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token != os.getenv('AUTH_TOKEN', 'default_fake_token'):
            return jsonify({"error": "Unauthorized"}), 401
        user = User.query.filter_by(username='test').first()
        return f(user, *args, **kwargs)
    return decorated