from quart import Blueprint, request
from quart_schema import validate_request, validate_response

from services.todo.todo_schemas import AddToDoRequestSchema, AddToDoResponseSchema, CompleteToDoRequestSchema, CompleteToDoResponseSchema


todo_route = Blueprint('todo_route', __name__, url_prefix="/todo")


@todo_route.route("/add", methods=["POST"])
@validate_request(AddToDoRequestSchema)
@validate_response(AddToDoResponseSchema)
async def add_todo(data):
    req_json = data.dict()
    print(req_json)

    return {
        'status': 'Add to do item successfully.'
    }, 200


@todo_route.route("/complete", methods=["PUT"])
@validate_request(CompleteToDoRequestSchema)
@validate_response(CompleteToDoResponseSchema)
async def Complete_todo(data):
    req_json = data.dict()
    print(req_json)

    return {
        'status': 'Completed to do item successfully.'
    }, 200
