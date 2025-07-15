from fastapi import FastAPI
from sqlalchemy import text
from app.database import Base, engine
from app.routers import sop

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(sop.router, prefix="/api")

@app.get("/ping")
def ping():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"msg": "pong"}
