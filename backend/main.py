from fastapi import FastAPI, WebSocket
import asyncio
import os

app = FastAPI()

images_dir = os.path.join(os.path.dirname(__file__), "images")
image_files = ["blue.png", "green.png", "red.png"]

images = []
for file in image_files:
    path = os.path.join(images_dir, file)
    with open(path, "rb") as f:
        images.append(f.read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    frame = 0
    while True:
        img_index = (frame // 20) % 3
        await websocket.send_bytes(images[img_index])
        frame += 1
        await asyncio.sleep(1/60)  # 60 FPS