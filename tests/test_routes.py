from fastapi import status
from fastapi.testclient import TestClient

from app.main import app
from app.service import ItemService, get_service

client = TestClient(app)


def get_service_test():
    return ItemService()


def test_cria_item():
    app.dependency_overrides[get_service] = get_service_test

    response = client.post(
        "/itemtodo",
        json={
            "titulo": "abc",
            "descricao": "123",
            "concluido": True,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "id": 0,
        "titulo": "abc",
        "descricao": "123",
        "concluido": True,
    }
