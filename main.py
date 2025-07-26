
from fastapi import FastAPI
from routers import device, channels, actions, videos, admin

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "YTFollow API พร้อมใช้งาน"}
  
app.include_router(device.router, prefix="/devices")
app.include_router(channels.router, prefix="/channels")
app.include_router(actions.router, prefix="/actions")
app.include_router(videos.router, prefix="/videos")
app.include_router(admin.router, prefix="/admin")
