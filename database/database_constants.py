import os

# DB_PATH = os.getenv("DB_PATH", os.path.join(os.path.dirname(__file__), "sqlite.db"))

USER = os.getenv("SUPABASE_USER")
PASSWORD = os.getenv("SUPABASE_PASSWORD")
HOST = os.getenv("SUPABASE_HOST")
PORT = os.getenv("SUPABASE_PORT")
DBNAME = os.getenv("SUPABASE_DBNAME")