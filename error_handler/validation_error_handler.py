from quart_schema import RequestSchemaValidationError, ResponseSchemaValidationError
from werkzeug.exceptions import BadRequest, InternalServerError

from logs.loggers import logger
from main import app


@app.errorhandler(RequestSchemaValidationError)
async def handle_error_request(error):
    logger.exception(f"Request Validation Error:\n{error}")
    return str(error.validation_error), BadRequest.code


@app.errorhandler(ResponseSchemaValidationError)
async def handle_error_response(error):
    logger.exception(f"Response Validation Error:\n{error}")
    return str(error.validation_error), InternalServerError.code
