import bcrypt
import sqlalchemy as sa
from database import engine

def authenticate_user(username, password):

    query = sa.text("""
    SELECT password_hash FROM users
    WHERE username=:username
    """)

    with engine.connect() as conn:
        result = conn.execute(query, {"username": username}).fetchone()

    if result:
        stored_hash = result[0]

        if bcrypt.checkpw(password.encode(), stored_hash.encode()):
            return True

    return False