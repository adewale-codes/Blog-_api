from sqlalchemy.orm import Session
from app.database.session import SessionLocal, engine

from app.users.models import User
from app.posts.models import Post
from app.comments.models import Comment

def reset_database():
    print("Dropping existing tables...")
    User.__table__.drop(engine)
    Post.__table__.drop(engine)
    Comment.__table__.drop(engine)

    print("Creating new tables...")
    User.__table__.create(engine)
    Post.__table__.create(engine)
    Comment.__table__.create(engine)

if __name__ == "__main__":
    print("Resetting the database...")
    reset_database()
    print("Database reset complete.")
