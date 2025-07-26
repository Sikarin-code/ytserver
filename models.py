
from pydantic import BaseModel
from typing import Literal

class DevicePing(BaseModel):
    device_id: str

class UninstallNotify(BaseModel):
    device_id: str

class ChannelItem(BaseModel):
    channel_id: str
    channel_name: str

class VideoItem(BaseModel):
    video_id: str
    channel_id: str
    title: str
    video_url: str

class SubscribeAction(BaseModel):
    device_id: str
    channel_id: str
    status: Literal['subscribed', 'unsubscribed']
