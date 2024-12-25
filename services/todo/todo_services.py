from quart import Blueprint


todo_route = Blueprint('todo_route', url_prefix='/todo')


@todo_route.route("/create", methods=["POST"])
async def create_todo():
    print('Nicely done brother')
    return
