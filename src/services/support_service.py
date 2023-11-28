from fastapi import APIRouter, Header

from src.api import app_base_url, Login
from src.constants.constants import ResponseMessage, ResponseStatus
from src.core.handlers.support_handler import SupportHandler
from src.logging import logger
from src.schemas.support_schema import *
from src.utilities.AESEnc import AESCipher

support_router = APIRouter(prefix=app_base_url)


@support_router.post(Login.support)
def support_fun(request_data: CustomerSupport, token: str = Header(...)):
    try:
        token_data = AESCipher.token_validation(token)
        support_object = SupportHandler()
        response = support_object.contact_support(request_data=request_data, user_email=token_data["email"])
        return response
    except Exception as e:
        logger.exception(f"Failed to Store support ticket- {e}")
        return ResponseMessage.final_json(ResponseStatus.failure, "Failed to store support ticket", data=None)

