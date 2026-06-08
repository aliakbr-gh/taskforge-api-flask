from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import register_controller, login_controller

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/auth/register", methods=["POST"])
def register():
    data = request.get_json()

    result, error = register_controller(data)

    if error:
        return jsonify({"message": error}), 400

    return jsonify({
        "message": "User registered successfully",
        "user": result
    })


@auth_bp.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()

    result, error = login_controller(data)

    if error:
        return jsonify({"message": error}), 401

    return jsonify({
        "message": "Login successful",
        "data": result
    })