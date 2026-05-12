import bcrypt
from sqlalchemy import text
from database import sql_con

def authenticate_user(username, password):

    query = text("""
    SELECT password_hash 
    FROM users 
    WHERE username=:username
    """)

    with sql_con.connect() as conn:
        result = conn.execute(query, {"username": username}).fetchone()

    if result:
        stored_hash = result[0]

        if bcrypt.checkpw(password.encode(), stored_hash.encode()):
            return True

    return False
def register_user(username, password):

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    query = text("""
    INSERT INTO users(username,password_hash)
    VALUES(:username,:password)
    """)

    try:
        with sql_con.begin() as conn:
            conn.execute(query,{
                "username": username,
                "password": hashed_password
            })
        return True
    except:
        return False