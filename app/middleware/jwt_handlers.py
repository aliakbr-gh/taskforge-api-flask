from flask import jsonify
from flask_jwt_extended import JWTManager
from app.utils.api_response import ApiResponse

jwt = JWTManager()

@jwt.unauthorized_loader
def missing_token_callback(error):
    response = ApiResponse.error_response(
        message="Authorization token is missing",
        status_code=401
    )
    return jsonify(response.to_dict()), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    response = ApiResponse.error_response(
        message="Invalid token",
        status_code=401
    )
    return jsonify(response.to_dict()), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    response = ApiResponse.error_response(
        message="Token expired",
        status_code=401
    )
    return jsonify(response.to_dict()), 401