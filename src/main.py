
from fastapi import FastAPI, status, Body

app = FastAPI()


messages_db = {"0": "First message"}


@app.get("/")
async def get_all_messages() -> dict:
    return messages_db


@app.get("/message/{message_id}")
async def get_message(message_id: str) -> str:
    pass


@app.post("/message", status_code=status.HTTP_201_CREATED)
async def create_message(message: str = Body()) -> str:
    current_index = len(messages_db)
    messages_db[current_index] = message
    return f"Message created!"


@app.put("/message/{message_id}")
async def update_message(message_id: str, message: str) -> str:
    pass


@app.delete("/message/{message_id}")
async def delete_message(message_id: str) -> str:
    pass


@app.delete("/")
async def kill_message_all() -> str:
    pass

