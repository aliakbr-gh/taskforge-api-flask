from app.utils.api_response import ApiResponse

def validate_login(data):
    if not data.get("email") or not data.get("password"):
        return ApiResponse.error_response(
            message="Email and password are required",
            status_code=400
        )

    return None