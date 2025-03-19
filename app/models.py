from pydantic import BaseModel


class ItemTodo(BaseModel):
    id: int
    titulo: str
    descricao: str
    concluido: bool = False


class ItemTodoPost(BaseModel):
    titulo: str
    descricao: str
    concluido: bool = False
