def validate_login(data):
    if "email" not in data:
        return False, "Email is required"

    if "password" not in data:
        return False, "Password is required"

    return True, None