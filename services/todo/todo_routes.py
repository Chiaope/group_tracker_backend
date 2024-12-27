from quart import Blueprint
from quart_schema import validate_querystring, validate_request, validate_response

from services.todo.todo_schemas import AddToDoRequestSchema, AddToDoResponseSchema, CompleteToDoRequestSchema, CompleteToDoResponseSchema, GetAllTodoResponseSchema, GetSingleTodoQuerySchema, GetSingleTodoResponseSchema
from services.todo.todo_services import add_todo_item, get_all_todo_item, get_single_todo_item


todo_route = Blueprint('todo_route', __name__, url_prefix="/todo")


@todo_route.route("/add", methods=["POST"])
@validate_request(AddToDoRequestSchema)
@validate_response(AddToDoResponseSchema)
async def add_todo_item_route(data):
    req_json = data.dict()
    add_todo_item(req_json)

    return {
        'status': 'Add to do item successfully.'
    }, 200


@todo_route.route("/all", methods=["GET"])
@validate_response(GetAllTodoResponseSchema)
async def get_all_todo_item_route():
    results = get_all_todo_item()

    return {
        'data': results
    }, 200


@todo_route.route("/single", methods=["GET"])
@validate_querystring(GetSingleTodoQuerySchema)
@validate_response(GetSingleTodoResponseSchema)
async def get_single_todo_item_route(query_args):
    todo_id = query_args.dict().get('todo_id', 0)
    results = get_single_todo_item(todo_id)

    return {
        'data': results
    }, 200


@todo_route.route("/complete", methods=["PUT"])
@validate_request(CompleteToDoRequestSchema)
@validate_response(CompleteToDoResponseSchema)
async def complete_todo_item_route(data):
    req_json = data.dict()
    print(req_json)

    return {
        'status': 'Completed to do item successfully.'
    }, 200
