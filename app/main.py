from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Travel AI Agent", version="0.1.0")

class ChatRequest(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"status": "ok", "service": "Travel AI Agent"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {"reply": "Travel AI Agent is running.", "message": req.message}
