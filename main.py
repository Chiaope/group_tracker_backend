from quart import Quart
from quart_schema import QuartSchema


app_name = "Group Tracker Backend"

app = Quart(app_name)
QuartSchema(app)

if __name__ == '__main__':
    from error_handler.http_error_handler import *
    from error_handler.validation_error_handler import *

    @app.route('/')
    async def default_route():
        return 'Default Route'

    from services.todo.todo_routes import todo_route
    app.register_blueprint(todo_route)

    app.run(debug=True)
