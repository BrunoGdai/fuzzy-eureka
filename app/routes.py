from fastapi import APIRouter, Depends, HTTPException, status

from app.exceptions import ItemNotFoundException
from app.models import ItemTodoPost
from app.service import ItemService, get_service

router = APIRouter()


@router.post("/itemtodo", status_code=status.HTTP_201_CREATED)
async def create_itemtodo(item: ItemTodoPost, service: ItemService = Depends(get_service)):
    return await service.cria_item(item)


@router.delete("/itemtodo/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_itemtodo(id: int, service: ItemService = Depends(get_service)):
    try:
        await service.apaga_item(id)
    except ItemNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id {id} was not found.")
