
from fastapi import APIRouter
from database import get_db
from models import ChannelItem

router = APIRouter()

@router.post("/add_primary")
def add_primary_channel(channel: ChannelItem):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO primary_channels (channel_id, channel_name) VALUES (?, ?)",
                (channel.channel_id, channel.channel_name))
    conn.commit()
    conn.close()
    return {"status": "added"}

@router.post("/add_secondary")
def add_secondary_channel(channel: ChannelItem):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO secondary_channels (channel_id, channel_name, submitted_by) VALUES (?, ?, ?)",
                (channel.channel_id, channel.channel_name, "user"))
    conn.commit()
    conn.close()
    return {"status": "added"}

@router.get("/primary")
def get_primary_channels():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM primary_channels")
    rows = cur.fetchall()
    conn.close()
    return {"channels": [dict(row) for row in rows]}

@router.get("/secondary")
def get_secondary_channels():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM secondary_channels")
    rows = cur.fetchall()
    conn.close()
    return {"channels": [dict(row) for row in rows]}
