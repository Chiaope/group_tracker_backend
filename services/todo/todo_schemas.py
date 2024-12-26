from datetime import datetime
from typing import Optional
from pydantic import BaseModel


# Request Schemas

class AddToDoRequestSchema(BaseModel):
    created_by: str
    created_timestamp: datetime
    title: str
    category: str
    note: Optional[str] = None


class CompleteToDoRequestSchema(BaseModel):
    completed_by: str
    completed_timestamp: datetime
    todo_id: int
    note: Optional[str] = None


# Response Schemas

class AddToDoResponseSchema(BaseModel):
    status: str


class CompleteToDoResponseSchema(BaseModel):
    status: str
