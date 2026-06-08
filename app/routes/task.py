from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.controllers.task_controller import (
    create_task_controller,
)

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/tasks", methods=["POST"])
@jwt_required()
def create_task_route():
    user_id = get_jwt_identity()
    data = request.get_json()

    response = create_task_controller(data, user_id)

    return jsonify(response.to_dict()), response.status_code