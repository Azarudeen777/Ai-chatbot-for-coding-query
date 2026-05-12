import pymysql
import os
from dotenv import load_env
from sqlalchemy import create_engine,text
import pandas as pd

load_dotenv()

# Fetch values
HOST = os.getenv("MYSQL_HOST")
USER = os.getenv("MYSQL_USER")
PASSWORD = os.getenv("MYSQL_PASSWORD")
DATABASE = os.getenv("MYSQL_DATABASE")


sql_con = create_engine(
    f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
)

try:
    sql_con
    print("database connected successfull")
except NameError:
    print("connecton failed")
