from werkzeug.exceptions import NotFound
from logs.loggers import logger
from main import app


@app.errorhandler(NotFound)
async def handle_404(error):
    logger.exception(f"Not Found Error:\n{error}")
    return NotFound.description, NotFound.code