from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db

router = APIRouter()

@router.get("/query-intent")
def query_intent(db: Session = Depends(get_db)):
    return {"message": "This endpoint will query the 'category' table in the database."}
