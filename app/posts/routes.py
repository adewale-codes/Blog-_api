from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.utils.pagination import paginate_items
from app.database.session import get_db
from app.posts import schemas, services, models
from app.authentication.auth import get_current_user

router = APIRouter()

@router.get("/posts", response_model=list[schemas.Post])
def read_posts(skip: int = Query(0, description="Skip items"), limit: int = Query(10, description="Number of items to return")):
    db = next(get_db()) 
    all_posts = services.get_posts(db, skip, limit)
    paginated_posts, total_pages = paginate_items(all_posts, page=skip, per_page=limit) 
    
    return {
        "data": paginated_posts,
        "page": skip,
        "total_pages": total_pages,
    }

@router.post("/posts", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    new_post = models.Post(**post.dict(), author_id=current_user.id)
    return services.create_post(db, new_post)

@router.get("/posts/{post_id}", response_model=schemas.Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = services.get_post(db, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.get("/posts", response_model=list[schemas.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return services.get_posts(db, skip, limit)

@router.patch("/posts/{post_id}", response_model=schemas.Post)
def update_post(post_id: int, post_update: schemas.PostUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    post = services.get_post(db, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only update your own posts")
    return services.update_post(db, post, post_update)

@router.delete("/posts/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    post = services.get_post(db, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only delete your own posts")
    services.delete_post(db, post)
    return post
