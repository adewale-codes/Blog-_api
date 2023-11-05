from sqlalchemy.orm import Session
from app.posts import models, schemas  

def create_post(db: Session, post: models.Post):
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Post).offset(skip).limit(limit).all()

def update_post(db: Session, post: models.Post, post_update: schemas.PostUpdate):
    for key, value in post_update.dict().items():
        setattr(post, key, value)
    db.commit()
    return post

def delete_post(db: Session, post: models.Post):
    db.delete(post)
    db.commit()
