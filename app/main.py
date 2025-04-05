
from fastapi import FastAPI
from fastapi.params import Body
#schema validation
from . import model
from .database import engine
from .routes import posts, users, auth, vote
from .config import settings

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "welcome to my API"}

