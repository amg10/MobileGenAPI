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

def generate_image(txt: str):
    image_path = "someimg.png"
    return image_path

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate_image")
async def get_image(text: str):
    image_path = Path(generate_image(text))
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)
