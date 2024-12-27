from datetime import datetime
from pydantic import BaseModel


# Todo Item Schema

class TodoItemSchema(BaseModel):
    id: int
    created_timestamp: datetime
    created_by: str
    title: str
    category: str
    note: str | None
    status: str


# Query Param Schema

class GetSingleTodoQuerySchema(BaseModel):
    todo_id: int


# Request Schemas

class AddToDoRequestSchema(BaseModel):
    created_by: str
    title: str
    category: str
    note: str | None = None


class CompleteToDoRequestSchema(BaseModel):
    completed_by: str
    completed_timestamp: datetime
    todo_id: int
    note: str | None = None


# Response Schemas

class GetAllTodoResponseSchema(BaseModel):
    data: list[TodoItemSchema]


class GetSingleTodoResponseSchema(BaseModel):
    data: TodoItemSchema | None


class AddToDoResponseSchema(BaseModel):
    status: str


class CompleteToDoResponseSchema(BaseModel):
    status: str
