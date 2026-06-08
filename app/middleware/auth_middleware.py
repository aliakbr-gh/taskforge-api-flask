# from functools import wraps
# from flask import jsonify
# from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
# from app.utils.api_response import ApiResponse

# def auth_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):

#         try:
#             verify_jwt_in_request()

#             user_id = get_jwt_identity()

#             kwargs["user_id"] = user_id

#             return fn(*args, **kwargs)

#         except Exception as e:
#             response = ApiResponse.error_response(
#                 message="Unauthorized access",
#                 status_code=401
#             )
#             return jsonify(response.to_dict()), 401

#     return wrapper