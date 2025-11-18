from functools import wraps
from flask import request, jsonify

def authenticate(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token != 'fake_token':
            return jsonify({"error": "Unauthorized"}), 401
        user = User.query.filter_by(username='test').first()
        return f(user, *args, **kwargs)
    return decorated
