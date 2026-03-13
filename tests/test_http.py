from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_book_endpoint():
    response = client.post("/books/", json={"title":"Hobbit","pages":300,"isbn":"321"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Hobbit"

def test_list_books_endpoint():
    #client.post("/books/", json={"title":"Dune","pages":500,"isbn":"456"})
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) >= 1