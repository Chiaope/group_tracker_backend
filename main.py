from logging.config import dictConfig
from quart import Quart

app_name = "Group Tracker Backend"

app = Quart(app_name)

if __name__ == '__main__':
    from error_handler.http_error_handler import *
    from logs.loggers import logger

    @app.route('/')
    async def default_route():
        logger.info('HRLLO WORLD')
        return 'Default Route'

    app.run(debug=True)