"""
Minimal server for testing AI chatbot functionality
"""

from fastapi import FastAPI, Depends, HTTPException, Header
from schemas import ChatRequest
from ai_chatbot import ai_chatbot

app = FastAPI(title="AI Chatbot Test Server")

def verify_jwt(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token")

    token = authorization.replace("Bearer ", "")
    
    # Phase-3 demo decode
    if token == "demo-token":
        return "demo-user"

    raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/api/{user_id}/chat")
def chat(
    user_id: str,
    req: ChatRequest,
    token_user: str = Depends(verify_jwt)
):
    if user_id != token_user:
        raise HTTPException(status_code=403, detail="Forbidden")

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
    uvicorn.run(app, host="0.0.0.0", port=8000)