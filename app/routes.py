from fastapi import APIRouter, Depends, status

from app.models import ItemTodoPost
from app.service import ItemService, get_service

router = APIRouter()


@router.post("/itemtodo", status_code=status.HTTP_201_CREATED)
async def create_itemtodo(item: ItemTodoPost, service: ItemService = Depends(get_service)):
    return await service.cria_item(item)
