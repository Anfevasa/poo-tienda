from fastapi import FastAPI
from app.api import category

app = FastAPI()

app.include_router(category.router, prefix="/api/v1/category", tags=["categories"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
