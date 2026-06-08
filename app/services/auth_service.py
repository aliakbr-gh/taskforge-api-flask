from app import db, bcrypt
from app.models.user import User
from flask_jwt_extended import create_access_token
from app.utils.api_response import ApiResponse

def register_user(name, email, password):
    user_exists = User.query.filter_by(email=email).first()

    if user_exists:
        return None, "User already exists"

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    new_user = User(
        name=name,
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return new_user, None

def login_user(email, password):
    user = User.query.filter_by(email=email).first()

    if not user:
        return ApiResponse.error_response("User not found", 404)

    if not bcrypt.check_password_hash(user.password, password):
        return ApiResponse.error_response("Invalid credentials", 401)

    token = create_access_token(identity=str(user.id))

    return ApiResponse.success_response(
        message="Login successful",
        data={"token": token}
    )