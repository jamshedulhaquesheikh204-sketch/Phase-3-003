from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from mcp_server import mcp  # Import the mcp instance from our new file
from mcp_tools.todo_tools import engine  # Use the same database setup as the tools
from sqlmodel import SQLModel
import os

# Create all tables
SQLModel.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/mcp", mcp)  # MCP server mounted

# Get API key from environment variable, fallback to hardcoded value (not recommended for production)
api_key = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

class ChatRequest(BaseModel):
    conversation_id: int | None = None
    message: str

class ChatResponse(BaseModel):
    conversation_id: int
    response: str

@app.post("/api/{user_id}/chat", response_model=ChatResponse)
def chat(user_id: str, req: ChatRequest):
    # Stateless message handling
    try:
        with open("specs/system_prompt.txt", "r") as f:
            system_prompt = f.read()
    except FileNotFoundError:
        system_prompt = "You are a helpful assistant."

    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # Using a valid OpenAI model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": req.message}
        ]
    )
    reply = completion.choices[0].message.content
    return {"conversation_id": req.conversation_id or 1, "response": reply}