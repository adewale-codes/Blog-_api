from pydantic import BaseModel

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    post_id: int

class CommentUpdate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
