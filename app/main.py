from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import memory

app = FastAPI()

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test")
def test():
    return {"message": "API working"}

app.include_router(memory.router)