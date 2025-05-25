from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path to the JSON data file (in the same directory as this file)
DATA_FILE = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")

# Helper to load the data file and return a name->marks dict
def load_marks():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return {item["name"]: item["marks"] for item in data}

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks_lookup = load_marks()
    result = [marks_lookup.get(name, None) for name in names]
    return JSONResponse(content={"marks": result})
