
from fastapi import APIRouter
from database import get_db
from models import SubscribeAction

router = APIRouter()

@router.post("/subscribe")
def report_subscribe(data: SubscribeAction):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO subscriptions (device_id, channel_id, status) VALUES (?, ?, ?)",
                (data.device_id, data.channel_id, data.status))
    conn.commit()
    conn.close()
    return {"status": "recorded"}
