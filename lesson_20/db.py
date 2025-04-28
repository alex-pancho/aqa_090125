import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
    except Error as e:
        print(f"Error: {e}")
    return conn

def close_connection(conn):
    """Close the SQLite database connection."""
    if conn:
        conn.close()
        print("Connection closed")
