
import sqlite3
import os

DB_PATH = "db/database.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            device_id TEXT PRIMARY KEY,
            online INTEGER DEFAULT 1,
            last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS primary_channels (
            channel_id TEXT PRIMARY KEY,
            channel_name TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS secondary_channels (
            channel_id TEXT PRIMARY KEY,
            channel_name TEXT,
            submitted_by TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            device_id TEXT,
            channel_id TEXT,
            status TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (device_id, channel_id)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS videos (
            video_id TEXT PRIMARY KEY,
            channel_id TEXT,
            title TEXT,
            video_url TEXT
        )
    """)

    conn.commit()
    conn.close()

if not os.path.exists("db"):
    os.mkdir("db")
if not os.path.exists(DB_PATH):
    init_db()
