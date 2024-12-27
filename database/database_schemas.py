from enum import Enum


class TodoItemTable(Enum):
    table_name = "todo_item_t"

    created_timestamp = "created_timestamp"
    created_by = "created_by"
    title = "title"
    category = "category"
    note = "note"
    status = "status"
