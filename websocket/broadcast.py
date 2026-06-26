from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        try:
            await websocket.accept()
            self.active_connections.append(websocket)

        except Exception as e:
            print(f"Connection Error: {e}")
    def disconnect(self, websocket: WebSocket):
        try:
            if websocket in self.active_connections:
                self.active_connections.remove(websocket)
        except Exception as e:
            print(f"Disconnect Error: {e}")
          
    async def broadcast(self, message: str):
        try:
            disconnected_clients = []
            for connection in self.active_connections:
                try:
                    await connection.send_text(message)
                except Exception:
                    disconnected_clients.append(connection)

            for connection in disconnected_clients:
                self.disconnect(connection)
        except Exception as e:
            print(f"Broadcast Error: {e}")


manager = ConnectionManager()