from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from broadcast import manager
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI(
    title="Week 3 Real-Time Communication API",
    version="1.0.0"
)
@app.get("/")
async def home():
    try:
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": "Welcome to Week 3 Real-Time Communication API",
                "data": None
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Internal Server Error",
                "error": str(e)
            }
        )

@app.get("/chat", response_class=HTMLResponse)
async def chat():
    try:
        with open("index.html", "r") as file:
            return HTMLResponse(file.read())
    except Exception as e:
        return HTMLResponse(f"<h2>{str(e)}</h2>")
    
@app.get("/events")
async def events():

    try:
        return StreamingResponse(
            event_generator(),
            media_type="text/event-stream"
        )
    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Unable to stream events",
                "error": str(e)
            }
        )

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    try:
        await manager.connect(websocket)
        while True:
            message = await websocket.receive_text()
            print(f"Received: {message}")
            await manager.broadcast(message)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("Client Disconnected")
    except Exception as e:
        manager.disconnect(websocket)
        print(f"Error: {e}")
        
async def event_generator():
    counter = 1
    while True:
        yield f"data: {counter}\n\n"
        counter += 1
        await asyncio.sleep(1)