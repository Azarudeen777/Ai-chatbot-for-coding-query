import bcrypt
import cryptography
from sqlalchemy import text
from database import sql_con

username = "admin"
password = "admin123"

# create hashed password
hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

query = text("""
INSERT INTO users(username,password_hash)
VALUES(:username,:password)
""")

with sql_con.begin() as conn:
    conn.execute(query,{
        "username": username,
        "password": hashed_password
    })

print("User created successfully")