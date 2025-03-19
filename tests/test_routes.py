from fastapi import status
from fastapi.testclient import TestClient

from app.main import app
from app.models import ItemTodo
from app.service import ItemService, get_service

client = TestClient(app)


async def get_service_test():
    return ItemService()


async def test_cria_item():
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
    app.dependency_overrides = {}


async def test_apaga_item_not_found():
    app.dependency_overrides[get_service] = get_service_test

    response = client.delete("/itemtodo/0")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Item with id 0 was not found."
    app.dependency_overrides = {}


async def test_apaga_item_no_content():
    service = get_service()
    service.lista = [ItemTodo(id=0, titulo="abc", descricao="qwe", concluido=True)]

    response = client.delete("/itemtodo/0")

    assert response.status_code == status.HTTP_204_NO_CONTENT
