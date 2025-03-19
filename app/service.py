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


service = None


def get_service():
    global service

    if not service:
        service = ItemService()

    return service
