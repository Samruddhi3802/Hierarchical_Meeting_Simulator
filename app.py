from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from main import simulate_meeting
import uvicorn
import os

app = FastAPI(title="AI Meeting Simulator API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MeetingRequest(BaseModel):
    topic: str

@app.post("/simulate")
async def run_simulation(request: MeetingRequest):
    if not request.topic.strip():
        raise HTTPException(status_code=400, detail="Topic cannot be empty")
    
    try:
        chat, usage = simulate_meeting(request.topic)
        
        print(f"\n{'='*30}")
        print(f"MEETING TOKEN USAGE: {usage}")
        print(f"{'='*30}\n")
        
        return {
            "chat_history": chat,
            "stats": {
                "total_tokens": usage.total_tokens,
                "prompt_tokens": usage.prompt_tokens,
                "completion_tokens": usage.completion_tokens,
                "successful_requests": usage.successful_requests
            }
        }
    except Exception as e:
        print(f"Error during simulation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001) 