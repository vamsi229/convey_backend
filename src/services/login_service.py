from fastapi import APIRouter, Header

from src.api import app_base_url, Login
from src.constants.constants import ResponseMessage, ResponseStatus
from src.core.handlers.login_handler import LoginHandler
from src.logging import logger
from src.schemas.login_schema import *
from src.utilities.AESEnc import AESCipher

login_router = APIRouter(prefix=app_base_url)


@login_router.post(Login.login)
def login_fun(request_data: login_model):
    try:
        login_object = LoginHandler()
        response = login_object.login_function(request_data=request_data)
        return response
    except Exception as e:
        logger.exception(f"Failed to Login- {e}")
        return ResponseMessage.final_json(ResponseStatus.failure, "Failed to login", data=None)


@login_router.post(Login.sign_up)
def signup_fun(request_data: signup_model):
    try:
        login_object = LoginHandler()
        response = login_object.signup_function(request_data=request_data)
        return response
    except Exception as e:
        logger.exception(f"Failed to Sign up the user- {e}")
        return ResponseMessage.final_json(ResponseStatus.failure, "Failed to Sign up the user", data=None)


@login_router.get(Login.get_user_details)
def get_user_fun(token: str = Header(...)):
    try:
        token_data = AESCipher.token_validation(token)
        login_object = LoginHandler()
        response = login_object.get_user_details(token_data)
        return response
    except Exception as e:
        logger.exception(f"Failed to get the user details- {e}")
        return ResponseMessage.final_json(ResponseStatus.failure, "Failed to get the user details", data=None)


@login_router.put(Login.update_user_details)
def update_user_fun(request_data: update_user_model,
                    token: str = Header(...)):
    try:
        token_data = AESCipher.token_validation(token)
        login_object = LoginHandler()
        response = login_object.update_user_details(request_data=request_data,
                                                    email=token_data["email"])
        return response
    except Exception as e:
        logger.exception(f"Failed to update the user details- {e}")
        return ResponseMessage.final_json(ResponseStatus.failure, "Failed to update the user details", data=None)


@login_router.put(Login.change_password)
def change_password_fun(request_data: change_password_model, token: str = Header(...)):
    try:
        token_data = AESCipher.token_validation(token)
        login_object = LoginHandler()
        response = login_object.change_password(request_data=request_data,
                                                    email=token_data["email"])
        return response
    except Exception as e:
        logger.exception(f"Failed to update the password in user details- {e}")
        return ResponseMessage.final_json(ResponseStatus.failure, "Failed to update the password in user details",
                                          data=None)
