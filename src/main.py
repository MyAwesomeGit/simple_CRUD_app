
from fastapi import FastAPI

app = FastAPI()


messages_db = {"0": "First message"}


@app.get("/")
async def get_all_messages() -> dict:
    pass


@app.get("/message/{message_id}")
async def get_message(message_id: str) -> str:
    pass


@app.post("/message")
async def create_message(message: str) -> str:
    pass


@app.put("/message/{message_id}")
async def update_message(message_id: str, message: str) -> str:
    pass


@app.delete("/message/{message_id}")
async def delete_message(message_id: str) -> str:
    pass


@app.delete("/")
async def kill_message_all() -> str:
    pass
