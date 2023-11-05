from fastapi.testclient import TestClient
from main import app
import json
from app.database import base
from app.database.session import SessionLocal

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Blog API"}

def test_create_user():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    }
    response = client.post("/users", json=user_data)
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"

def test_create_post():
    post_data = {
        "title": "Test Post",
        "content": "This is a test post content."
    }
    response = client.post("/posts", json=post_data)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Post"

def test_create_comment():
    comment_data = {
        "text": "This is a test comment",
        "post_id": 1
    }
    response = client.post("/comments", json=comment_data)
    assert response.status_code == 201
    assert response.json()["text"] == "This is a test comment"

def test_get_comments_by_post_id():
    response = client.get("/comments/1")
    assert response.status_code == 200
    assert len(response.json()) > 0
