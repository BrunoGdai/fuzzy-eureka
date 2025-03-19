import pytest

from app.exceptions import ItemNotFoundException
from app.models import ItemTodo, ItemTodoPost
from app.service import ItemService, get_service


async def test_cria_item():
    item = ItemTodoPost(titulo="abc", descricao="qwe", concluido=True)
    service = ItemService()
    service.lista = []
    res = await service.cria_item(item)

    assert res == ItemTodo(id=0, titulo=item.titulo, descricao=item.descricao, concluido=item.concluido)


async def test_cria_item_multiplos():
    item = ItemTodoPost(titulo="abc", descricao="qwe", concluido=True)
    service = ItemService()
    service.lista = []
    res = await service.cria_item(item)
    assert res == ItemTodo(id=0, titulo=item.titulo, descricao=item.descricao, concluido=item.concluido)

    res = await service.cria_item(item)
    assert res == ItemTodo(id=1, titulo=item.titulo, descricao=item.descricao, concluido=item.concluido)


async def test_apaga_item():
    item = ItemTodo(id=0, titulo="abc", descricao="qwe", concluido=True)
    service = ItemService()
    service.lista = [item]

    await service.apaga_item(0)

    assert len(service.lista) == 1
    assert service.lista[0] is None


async def test_apaga_multiplos_itens():
    item = ItemTodo(id=0, titulo="abc", descricao="qwe", concluido=True)
    item2 = ItemTodo(id=1, titulo="kkk", descricao="risos", concluido=True)
    service = ItemService()
    service.lista = [item, item2]

    await service.apaga_item(0)

    assert item not in service.lista
    assert service.lista[0] is None
    assert service.lista[1] == item2

    await service.apaga_item(1)

    assert item2 not in service.lista
    assert service.lista[0] is None
    assert service.lista[1] is None


async def test_apaga_item_twice():
    item = ItemTodo(id=0, titulo="abc", descricao="qwe", concluido=True)
    item2 = ItemTodo(id=1, titulo="kkk", descricao="risos", concluido=True)
    service = ItemService()
    service.lista = [item, item2]

    await service.apaga_item(0)

    assert item not in service.lista
    assert service.lista[0] is None
    assert service.lista[1] == item2

    with pytest.raises(ItemNotFoundException):
        await service.apaga_item(0)

    assert item2 in service.lista
    assert service.lista[0] is None
    assert service.lista[1] == item2


async def test_apaga_item_inexistente():
    item = ItemTodo(id=0, titulo="abc", descricao="qwe", concluido=True)
    item2 = ItemTodo(id=1, titulo="kkk", descricao="risos", concluido=True)
    service = ItemService()
    service.lista = [item, item2]

    with pytest.raises(ItemNotFoundException):
        await service.apaga_item(5)

    assert service.lista[0] == item
    assert service.lista[1] == item2


async def test_apaga_item_vazio():
    service = ItemService()

    with pytest.raises(ItemNotFoundException):
        await service.apaga_item(0)


async def test_get_service():
    service = None  # noqa
    res = get_service()

    assert isinstance(res, ItemService)


async def test_get_service_existente():
    res = get_service()

    assert isinstance(res, ItemService)
