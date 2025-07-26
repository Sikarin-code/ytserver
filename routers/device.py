
from fastapi import APIRouter
from database import get_db
from models import DevicePing, UninstallNotify

router = APIRouter()

@router.post("/ping")
def ping_device(data: DevicePing):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO devices (device_id, online) VALUES (?, ?)", (data.device_id, 1))
    conn.commit()
    conn.close()
    return {"status": "ok"}

@router.post("/uninstall")
def uninstall_device(data: UninstallNotify):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE devices SET online = 0 WHERE device_id = ?", (data.device_id,))
    cur.execute("DELETE FROM secondary_channels WHERE submitted_by = ?", (data.device_id,))
    conn.commit()
    conn.close()
    return {"status": "removed"}
