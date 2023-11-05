from sqlalchemy.orm import Session
from app.comments import models

def create_comment(db: Session, comment: models.Comment):
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def update_comment(db: Session, comment: models.Comment, comment_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not db_comment:
        return None
    for key, value in comment.dict().items():
        setattr(db_comment, key, value)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
        return db_comment
    return None
