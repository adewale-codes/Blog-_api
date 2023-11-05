from sqlalchemy.orm import Session
from app.database.session import SessionLocal, engine
from app.users.models import User
from app.config import settings

def init_database():
    User.__table__.create(engine)

    db = SessionLocal()
    user = User(
        username=settings.INITIAL_USER_USERNAME,
        email=settings.INITIAL_USER_EMAIL,
        password=settings.INITIAL_USER_PASSWORD,
        is_admin=True,
    )
    db.add(user)
    db.commit()
    db.close()

if __name__ == "__main__":
    print("Initializing the database...")
    init_database()
    print("Database initialization complete.")
