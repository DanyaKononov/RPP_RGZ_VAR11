from flask import request, jsonify
from .models import db, User, Resource, Policy
from .auth import authenticate
from .abac import check_access

def init_routes(app):
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        # TODO: Validate and create user
        return jsonify({"message": "User registered"}), 201

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        # TODO: Authenticate user
        return jsonify({"token": "fake_token"}), 200

    @app.route('/resources', methods=['POST'])
    def add_resource():
        data = request.get_json()
        # TODO: Add resource and policies
        return jsonify({"message": "Resource added"}), 201

    @app.route('/resources', methods=['GET'])
    @authenticate
    def list_resources(user):
        resources = Resource.query.all()
        accessible = [r for r in resources if check_access(user, r)]
        return jsonify([{"name": r.name} for r in accessible]), 200

    @app.route('/resources/<int:resource_id>', methods=['GET'])
    @authenticate
    def get_resource(user, resource_id):
        resource = Resource.query.get_or_404(resource_id)
        if check_access(user, resource):
            return jsonify({"name": resource.name}), 200
        return jsonify({"error": "Access denied"}), 403
