from werkzeug.exceptions import NotFound, BadRequest, InternalServerError
from logs.loggers import logger
from main import app


@app.errorhandler(NotFound)
async def handle_error_not_found(error):
    logger.exception(f"Not Found Error:\n{error}")
    return NotFound.description, NotFound.code


@app.errorhandler(BadRequest)
async def handle_error_bad_request(error):
    logger.exception(f"Bad Request Error:\n{error}")
    return BadRequest.description, BadRequest.code


@app.errorhandler(InternalServerError)
async def handle_error_internal_server(error):
    logger.exception(f"Internal Server Error:\n{error}")
    return InternalServerError.description, InternalServerError.code
