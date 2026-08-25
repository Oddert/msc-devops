"""Contains reusable hashing functions to parse and compare passwords."""

import bcrypt


def get_hashed_pwd(password: str):
    """Creates a hashed password for storage in the database."""
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt).decode()


def verify_hashed_pwd(password: str, hashed_password: bytes):
    """Compares a user-entered password to a retrieved hashed password."""
    password_bytes = password.encode('utf-8')
    if bcrypt.checkpw(password_bytes, hashed_password):
        return True
    return False
