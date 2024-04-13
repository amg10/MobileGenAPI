from fastapi import FastAPI, Response, Form
from fastapi.responses import StreamingResponse, FileResponse
from typing import Optional
import tempfile
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Example function to generate video from text (replace with your actual implementation)
def generate_video(text: str):
    # Your video generation logic here
    # This is just a placeholder
    video_file_path = "stop_motion_video.mp4"
    return video_file_path

def generate_image(txt: str):
    image_path = "someimg.png"
    return image_path


@app.post("/generate_video/")
async def generate_text_to_video(text: str = Form(...)):
    # Generate video from text
    video_path = generate_video(text)
    
    # Open video file and read it as bytes
    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()
    
    return Response(content=video_bytes, media_type="video/mp4")

@app.post("/stream_generate_video/")
async def stream_video(text: str = Form(...)):

    def stream_video():
        with open(generate_video(text), "rb") as video_file:
            yield from video_file

    return StreamingResponse(stream_video(), media_type="video/mp4")

@app.post("/generate_image")
async def get_image(text: str):
    image_path = Path(generate_image(text))
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)