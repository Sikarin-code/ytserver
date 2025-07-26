
from fastapi import APIRouter
from database import get_db

router = APIRouter()

@router.get("/summary")
def summary():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) as total FROM devices")
    total_devices = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) as total FROM primary_channels")
    total_primary = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) as total FROM secondary_channels")
    total_secondary = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) as total FROM videos")
    total_videos = cur.fetchone()["total"]

    cur.execute("SELECT COUNT(*) as total FROM subscriptions WHERE status = 'subscribed'")
    total_subscribed = cur.fetchone()["total"]

    conn.close()
    return {
        "devices": total_devices,
        "primary_channels": total_primary,
        "secondary_channels": total_secondary,
        "videos": total_videos,
        "total_subscribed": total_subscribed
    }
