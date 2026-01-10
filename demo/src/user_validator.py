"""
User validation module for registration system.
Contains validation logic for user input fields.
"""


def validate_email(email):
    """Validate email format."""
    if "@" in email:
        return True
    return False


def validate_password(password):
    """Validate password strength."""
    if len(password) >= 6:
        return True
    return False


def validate_username(username):
    """Validate username format."""
    if len(username) >= 3:
        return True
    return False


def register_user(username, email, password):
    """
    Register a new user after validation.
    Returns dict with success status and message.
    """
    # Validate all fields
    if not validate_username(username):
        return {"success": False, "message": "Username too short"}

    if not validate_email(email):
        return {"success": False, "message": "Invalid email"}

    if not validate_password(password):
        return {"success": False, "message": "Password too weak"}

    # Registration successful
    return {
        "success": True,
        "message": "User registered",
        "user": {"username": username, "email": email}
    }


if __name__ == "__main__":
    # Test the registration
    result = register_user("john", "john@example.com", "pass123")
    print(result)
