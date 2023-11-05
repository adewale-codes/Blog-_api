from fastapi import FastAPI, HTTPException
from app.database.session import SessionLocal, engine
from app.database.base import Base
from app.config import settings
from app.errors.handlers import custom_exception_handler
from app.users.routes import router as user_router
from app.posts.routes import router as post_router
from app.comments.routes import router as comment_router
from app.authentication.routes import router as auth_router
from app.authentication.auth import oauth2_scheme
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(HTTPException, custom_exception_handler)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup_db_client():
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown_db_client():
    db = SessionLocal()
    db.close()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(post_router, prefix="/posts", tags=["posts"])
app.include_router(comment_router, prefix="/comments", tags=["comments"])
app.include_router(auth_router, prefix="/auth", tags=["authentication"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
