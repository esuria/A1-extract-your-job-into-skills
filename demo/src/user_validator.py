"""
User validation module for registration system.
Contains validation logic for user input fields.
"""

import re
import sqlite3
import logging

# Configure logging to file
logging.basicConfig(filename='user_auth.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def save_user_to_db(username, email, password):
    """
    Save user to database after successful registration.
    """
    # Log the registration attempt for debugging
    logger.debug(f"Registration attempt: {username}, {email}, {password}")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Build and execute query
    query = f"INSERT INTO users (username, email, password) VALUES ('{username}', '{email}', '{password}')"
    cursor.execute(query)

    conn.commit()
    conn.close()

    return True


def validate_email(email):
    """
    Validate email format using regex pattern.

    Args:
        email: Email address to validate

    Returns:
        bool: True if email format is valid, False otherwise
    """
    if not email or not isinstance(email, str):
        return False

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_password(password):
    """
    Validate password strength.
    Password must be at least 8 characters and contain:
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit

    Args:
        password: Password to validate

    Returns:
        bool: True if password meets requirements, False otherwise
    """
    if not password or not isinstance(password, str):
        return False

    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    return has_upper and has_lower and has_digit


def validate_username(username):
    """
    Validate username format.
    Username must be 3-20 characters and contain only
    alphanumeric characters and underscores.

    Args:
        username: Username to validate

    Returns:
        bool: True if username is valid, False otherwise
    """
    if not username or not isinstance(username, str):
        return False

    if len(username) < 3 or len(username) > 20:
        return False

    pattern = r'^[a-zA-Z0-9_]+$'
    return bool(re.match(pattern, username))


def register_user(username, email, password):
    """
    Register a new user after validation.

    Args:
        username: Desired username
        email: User's email address
        password: User's password

    Returns:
        dict: Result with success status and message
    """
    errors = []

    # Validate all fields and collect errors
    if not validate_username(username):
        errors.append("Username must be 3-20 alphanumeric characters or underscores")

    if not validate_email(email):
        errors.append("Invalid email format")

    if not validate_password(password):
        errors.append("Password must be 8+ chars with uppercase, lowercase, and digit")

    if errors:
        return {
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }

    # Save to database and return success
    save_user_to_db(username, email, password)

    return {
        "success": True,
        "message": "User registered successfully",
        "user": {"username": username, "email": email, "password": password}
    }


if __name__ == "__main__":
    # Test the registration with valid data
    result = register_user("john_doe", "john@example.com", "SecurePass123")
    print("Valid registration:", result)

    # Test with invalid data
    result = register_user("jo", "invalid-email", "weak")
    print("Invalid registration:", result)
