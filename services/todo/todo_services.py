from pprint import pprint
from database.database_schemas import TodoItemTable
from database.database_services import execute_query


def add_todo_item(data):
    print(f"Todo Item:\n")
    pprint(data)
    execute_query(f"""
                    INSERT INTO {TodoItemTable.table_name.value}
                    ({TodoItemTable.created_by.value}, {TodoItemTable.title.value}, {TodoItemTable.category.value}, {TodoItemTable.note.value})
                    VALUES
                    (%(created_by)s, %(title)s, %(category)s, %(note)s)
                    """, data)
    return


def get_all_todo_item():
    results = execute_query(f"""
                            SELECT * FROM {TodoItemTable.table_name.value}
                            """)
    return results


def get_single_todo_item(todo_id):
    results = execute_query(f"""
                            SELECT * FROM {TodoItemTable.table_name.value}
                            WHERE id = %(todo_id)s
                            """, {'todo_id': todo_id}, fetch_one=True)
    return results
