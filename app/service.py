from app.exceptions import ItemNotFoundException
from app.models import ItemTodo, ItemTodoPost


class ItemService:
    def __init__(self):
        self.lista = []

    async def cria_item(self, item: ItemTodoPost):
        item_novo = ItemTodo(
            id=len(self.lista),
            titulo=item.titulo,
            descricao=item.descricao,
            concluido=item.concluido,
        )

        self.lista.append(item_novo)
        return item_novo

    async def apaga_item(self, id: int):
        if id >= 0 and id < len(self.lista) and self.lista[id]:
            self.lista[id] = None
            return
        raise ItemNotFoundException()


service = None


def get_service():
    global service

    if not service:
        service = ItemService()

    return service
