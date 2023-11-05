from fastapi import APIRouter, Depends, HTTPException, status, Path, Query
from sqlalchemy.orm import Session
from app.comments import schemas, services
from app.database.session import get_db
from app.authentication.auth import get_current_user
from app.users import models as user_models

router = APIRouter()

@router.post("/create", response_model=schemas.Comment)
def create_comment(
    comment: schemas.CommentCreate,
    db: Session = Depends(get_db),
    current_user: user_models.User = Depends(get_current_user),
):
    return services.create_comment(db, comment, current_user)

@router.patch("/update/{comment_id}", response_model=schemas.Comment)
def update_comment(
    comment_id: int = Path(..., title="Comment ID"),
    comment_update: schemas.CommentUpdate = None,  
    db: Session = Depends(get_db),
    current_user: user_models.User = Depends(get_current_user),
):
    comment = services.get_comment(db, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this comment")
    return services.update_comment(db, comment, comment_update)

@router.delete("/delete/{comment_id}")
def delete_comment(
    comment_id: int = Path(..., title="Comment ID"),
    db: Session = Depends(get_db),
    current_user: user_models.User = Depends(get_current_user),
):
    comment = services.get_comment(db, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this comment")
    services.delete_comment(db, comment_id)
    return {"detail": "Comment deleted"}
