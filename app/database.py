from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port
                                                                                                                                 }/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

def drop_all_connections():
    conn = psycopg2.connect("dbname=postgres user=postgres password=1968 host=localhost")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""
        SELECT pg_terminate_backend(pg_stat_activity.pid)
        FROM pg_stat_activity
        WHERE pg_stat_activity.datname = 'health'
        AND pid <> pg_backend_pid();
    """)
    cur.close()
    conn.close()

# Drop old connections before creating a new engine
drop_all_connections()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try: 
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
#                                 password='1968', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Databse Connection Successful")
#         break
#     except Exception as error:
#         print("Database connection unsucessful")
#         print(f"Error: {error}")
#         time.sleep(2)

