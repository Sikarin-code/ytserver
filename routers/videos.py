
from fastapi import APIRouter
from database import get_db
from models import VideoItem

router = APIRouter()

@router.post("/add")
def add_video(video: VideoItem):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO videos (video_id, channel_id, title, video_url) VALUES (?, ?, ?, ?)",
                (video.video_id, video.channel_id, video.title, video.video_url))
    conn.commit()
    conn.close()
    return {"status": "video added"}

@router.post("/delete")
def delete_video(video: VideoItem):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM videos WHERE video_id = ?", (video.video_id,))
    conn.commit()
    conn.close()
    return {"status": "video deleted"}

@router.get("/list")
def list_all_videos():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM videos")
    rows = cur.fetchall()
    conn.close()
    return {"videos": [dict(row) for row in rows]}
