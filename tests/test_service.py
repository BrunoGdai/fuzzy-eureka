from app.models import ItemTodo, ItemTodoPost
from app.service import ItemService


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
