from app.services.auth_service import register_user, login_user
from app.validators.auth_validator import validate_login


def register_controller(data):
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    user, error = register_user(name, email, password)

    if error:
        return None, error

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }, None


def login_controller(data):
    email = data.get("email")
    password = data.get("password")
    
    validation_error = validate_login(data)

    if validation_error:
        return validation_error

    token, error = login_user(email, password)

    if error:
        return None, error

    return {
        "token": token
    }, None