"""
Debug server for testing AI chatbot functionality
"""

from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel
from ai_chatbot import ai_chatbot

app = FastAPI(title="AI Chatbot Debug Server")

class ChatRequest(BaseModel):
    message: str

def verify_jwt(authorization: str = Header(None)):
    print(f"Received authorization header: {authorization}")  # Debug line
    if not authorization or not authorization.startswith("Bearer "):
        print("Authorization header missing or doesn't start with 'Bearer '")  # Debug line
        raise HTTPException(status_code=401, detail="Invalid token")

    token = authorization.replace("Bearer ", "")
    print(f"Extracted token: {token}")  # Debug line
    
    # Phase-3 demo decode
    if token == "demo-token":
        print("Valid demo token received")  # Debug line
        return "demo-user"

    print("Invalid token")  # Debug line
    raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/api/{user_id}/chat")
def chat(
    user_id: str,
    req: ChatRequest,
    token_user: str = Depends(verify_jwt)
):
    print(f"User ID from URL: {user_id}")  # Debug line
    print(f"Token user: {token_user}")  # Debug line
    if user_id != token_user:
        print(f"User ID mismatch: {user_id} != {token_user}")  # Debug line
        raise HTTPException(status_code=403, detail="Forbidden")

    print(f"Processing message: {req.message}")  # Debug line
    # ✅ AI CHATBOT IS ALLOWED HERE
    response = ai_chatbot.process(
        user_id=user_id,
        message=req.message
    )

    return {
        "response": response
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)