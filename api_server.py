from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

latest_data = {}

@app.get("/")
def root():
    # Read the HTML file and return it
    with open("dashboard.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/data")
async def receive_data(request: Request):
    data = await request.json()
    
    gateway_id = data.get("gateway_id", "unknown")
    latest_data[gateway_id] = data
    latest_data[gateway_id]["received_at"] = datetime.datetime.now().isoformat()

    print(f"Received data from {gateway_id}")
    return {"status": "ok"}

@app.get("/dashboard")
def dashboard():
    return latest_data
