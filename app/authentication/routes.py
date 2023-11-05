from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.authentication.auth import create_access_token, get_current_user
from app.users import schemas as user_schemas

router = APIRouter()

@router.post("/login", response_model=dict)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    token = create_access_token(data={"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/users/me", response_model=user_schemas.User)
def read_users_me(current_user: user_schemas.User = Depends(get_current_user)):
    return current_user
