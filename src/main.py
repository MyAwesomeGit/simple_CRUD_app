
from fastapi import FastAPI, status, Body
from typing import List
from message import Message

app = FastAPI()

messages_db = []


@app.get("/")
async def get_all_messages() -> List[Message]:
    return messages_db


@app.get("/message/{message_id}")
async def get_message(message_id: int)  -> Message:
    return messages_db[message_id]


@app.post("/message", status_code=status.HTTP_201_CREATED)
async def create_message(message: Message) -> str:
    if messages_db:
        message.id = max(messages_db, key=lambda m: m.id).id + 1
    else:
        message.id = 0
    messages_db.append(message)
    return f"Message created!"


@app.put("/message/{message_id}")
async def update_message(message_id: str, message: str = Body()) -> str:
    edit_message = messages_db[message_id]
    edit_message.text = message
    return f"Message updated!"


@app.delete("/message/{message_id}")
async def delete_message(message_id: int) -> str:
    messages_db.pop(message_id)
    return f"Message ID={message_id} deleted!"


@app.delete("/")
async def delete_all_messages() -> str:
    messages_db.clear()
    return "All messages deleted!"
